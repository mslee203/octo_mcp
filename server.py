from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("selta-octo")

def dummyTool(param: str) -> str:
    """
    Method description here.
    """
    # Do Some Processing Here
    return f"Your tool will return processed {param}"

@mcp.tool()
async def dummy_tool(param: str) -> str:
    """
    Definition of a tool here.
    """
    # Do some awsome processing here
    awsome_response = dummyTool(param)
    if not awsome_response:
        return "No awsome response found."

    return 

if __name__ == "__main__":
    mcp.run(transport="stdio")