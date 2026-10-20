from crewai import Task


def create_tasks(
    head_planner,
    research_agent,
    analyst_agent,
    strategy_agent,
):
    planning_task = Task(
        description=(
            "Create a structured GTM research brief for the following product or "
            "business idea: {business_idea}. Define the target market, research "
            "questions, assumptions, and required outputs."
        ),
        expected_output=(
            "A structured research brief with objectives, scope, assumptions, "
            "research questions, and success criteria."
        ),
        agent=head_planner,
    )

    research_task = Task(
        description=(
            "Research the market for {business_idea}. Use the available search "
            "tool for current information. Investigate customer segments, "
            "competitors, pain points, market trends, pricing signals, and "
            "buying behavior. Cite the URL for every externally verifiable claim. "
            "Do not invent statistics or sources. Separate verified findings, "
            "assumptions, and open questions."
        ),
        expected_output=(
            "A structured research report with these sections:\n"
                "1. Executive summary\n"
                "2. Customer segments\n"
                "3. Customer pain points\n"
                "4. Competitors\n"
                "5. Market trends\n"
                "6. Evidence and source URLs\n"
                "7. Assumptions\n"
                "8. Open questions"
        ),
        agent=research_agent,
        context=[planning_task],
    )

    analysis_task = Task(
        description=(
            "Analyze the planning brief and research report. Identify the most "
            "important market opportunities, risks, customer segments, competitive "
            "implications, and strategic conclusions."
        ),
        expected_output=(
            "A concise analytical report with key insights, prioritized opportunities, "
            "risks, trade-offs, and recommendations."
        ),
        agent=analyst_agent,
        context=[planning_task, research_task],
    )

    strategy_task = Task(
        description=(
            "Develop a practical GTM plan using the research and analysis. Include "
            "ideal customer profile, positioning, messaging, pricing considerations, "
            "distribution channels, launch phases, KPIs, and risks."
        ),
        expected_output=(
            "A structured GTM plan with target segments, positioning, messaging, "
            "channels, launch actions, KPIs, assumptions, and risk mitigations."
        ),
        agent=strategy_agent,
        context=[planning_task, research_task, analysis_task],
    )

    return [
        planning_task,
        research_task,
        analysis_task,
        strategy_task,
    ]

