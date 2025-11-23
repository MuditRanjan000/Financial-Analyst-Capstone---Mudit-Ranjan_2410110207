import operator
from typing import Annotated, List, TypedDict

class GraphState(TypedDict):
    """
    Represents the state of our Financial Analyst Graph.

    Attributes:
        company_name: The name of the company to research (Input).
        stock_data: Raw text or dict containing price/volume data.
        news_articles: A list of summaries or snippets from news search.
        final_report: The generated analysis (Output).
    """
    company_name: str
    stock_data: str
    # We use 'operator.add' (reducer) so that if multiple nodes find news, 
    # we can just append to this list instead of overwriting it.
    news_articles: Annotated[List[str], operator.add]
    final_report: str