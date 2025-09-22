from mcp.server.fastmcp import FastMCP
from smithery.decorators import smithery

@smithery.server()
def create_server():
    """Create and return a FastMCP server instance."""
    
    server = FastMCP(name="selta-octo")

    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiplies two numbers together."""
        return a * b

    return server