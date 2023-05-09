# Note: The openai-python library support for Azure OpenAI is in preview.
import os
import sys
import typer
import openai
import yaml
import orjson

openai.api_type = "azure"
openai.api_base = "https://southcentralus.api.cognitive.microsoft.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

# establish a typer app
app = typer.Typer()


# use the httpx library to make a request to the PubMed API
# to get the abstract for a given PMID
def get_abstract(pmid: int):
    import httpx

    r = httpx.get(
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=text&rettype=abstract"
    )
    return r.text


def _prepare_message(pmid: int):
    abstract = get_abstract(pmid)
    messages = []
    messages.append(
        {
            "role": "system",
            "content": """
            You are a cancer center program administrator. You are presented with titles and abstracts of publications and your job is to determine if the associated paper is cancer-related or not. Include an estimate of your confidence in terms of a number between 1 and 5, with 5 being most confident in classification and 1 being not sure at all. Include the medically-related concepts, a short (1-sentence) definition or description of the term, and whether or not the term is cancer-related or not as a list in YAML format. Express your results like so:\n\ncancer-related: <Yes|No> \nconficence: <1-5>\nconcepts:\n  - concept: <concept 1>\n    concept_description: <description of concept 1>\n    cancer-related: <Yes|No>\n  - concept: <concept 2>\n    concept_description: <description of concept 2>\n    cancer-related: <Yes|No>\n\nNow I will present you with the title and abstract like this:\n\n<abstract and title>\n""",
        }
    )

    messages.append({"role": "system", "content": f"{abstract}"})
    messages.append({"role": "user", "content": f"abstract"})
    return messages


def _prepare_results(pmid: int, response: dict):
    result = yaml.load(
        response["choices"][0]["message"]["content"], Loader=yaml.FullLoader
    )
    result["pmid"] = pmid
    return result


@app.command()
def perform_completion(pmid: int):
    """
    Use the OpenAI API to classify a PubMed abstract as cancer-related or
    not.The output is a json object with the following structure that includes
    the pmid, the cancer-related classification, the confidence, and the
    concepts that were found in the abstract.
    """

    messages = _prepare_message(pmid)

    response = openai.ChatCompletion.create(
        engine="autogpt-best",
        messages=messages,
        temperature=0.7,
        max_tokens=800,
        top_p=0.99,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )
    result = _prepare_results(pmid, response)  # type: ignore
    sys.stdout.buffer.write(orjson.dumps(result) + b"\n")


if __name__ == "__main__":
    app()
