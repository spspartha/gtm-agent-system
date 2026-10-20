from gtm_agents.crew import create_gtm_crew


if __name__ == "__main__":
    crew = create_gtm_crew()

    result = crew.kickoff(
        inputs={
            "business_idea": (
                "A SaaS platform that helps small businesses automate "
                "customer feedback analysis."
            )
        }
    )

    print("\n=== Final GTM Plan ===\n")
    print(result)

