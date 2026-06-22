from agents import build_search_agent, build_scrape_agent, writer_chain, critic_chain
def run_research_pipeline(topic : str)-> dict:
    state = {}
    #search agent working
    print("\n"+"=" * 50)
    print("Step 1 - search agent is working..")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages":[{"role": "user", "content": f"Find recent detailed and reliable information on the topic: {topic}"}]
    })
    state["search_result"] = search_result['messages'][-1].content
    print("\n search result" ,state['search_result'])

    #step 2 - scrape agent working
    print("\n"+"=" * 50)
    print("Step 2 - Scrape agent is working..") 
    print("="*50)
    
    scrape_agent = build_scrape_agent()
    scrape_result = scrape_agent.invoke({
        "messages": [{
            "role": "user",
            "content": (
                f"Based on the following search results about '{topic}',"
                f" pick the most relevant URLs and scrape them for deeper reading. Return the clean text content of each URL.\n\n"
                f"Search Results:\n{state['search_result'][:800]}"
            )
        }]
    })

    state['scraped_content'] = scrape_result['messages'][-1].content
    print("\n Scraped content", state['scraped_content'])

    #step 3 - writer chain working
    print("\n"+"=" * 50)
    print("Step 3 - Writer chain is working..")     
    print("="*50)

    research_combined = (
        f"Search Results:\n{state['search_result']}\n\n"
        f"Scraped Content:\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Research report generated:\n", state['report'])

    #critic report
    print("\n"+"=" * 50)
    print("Step 4 - Critic chain is reviewing the report.") 
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })
    print("\n Critic report \n", state['feedback'])

    return state


if __name__ == "__main__":
    topic = input("Enter the research topic: ")
    run_research_pipeline(topic)