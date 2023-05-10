import typer
import orjson
from pubmed_cancer_classifier import perform_completion

app = typer.Typer()

@app.command()
def classify_pmid(pmid: int):
    """
    Use the OpenAI API to classify a PubMed abstract as cancer-related or
    not.The output is a json object with the following structure that includes
    the pmid, the cancer-related classification, the confidence, and the
    concepts that were found in the abstract.
    """
    result = perform_completion(pmid)
    typer.echo(orjson.dumps(result))

if __name__ == "__main__":
    app()

