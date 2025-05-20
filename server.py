from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("MCP-count-total-rs",
              host = "127.0.0.1",
              port = 8080,
              timeout = 30)

@mcp.tool()
def count_total_rs(text: str) -> int:
    """Count the total number of Rs in a given string
    Input:
        text: str --> The text to count the Rs in
    Output:
        count: int --> The total number of Rs in the given string
    """
    if not isinstance(text, str):
        raise ValueError("Text must be a string")
    
    return text.lower().count("r")

if __name__ == "__main__":
    print("Starting MCP server at http://127.0.0.1:8080 on port 8080")
    mcp.run()
