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
            "Using the research brief, investigate the target customers, market "
            "context, competitors, customer pain points, and relevant trends. "
            "Do not invent facts. Label assumptions and identify evidence gaps."
        ),
        expected_output=(
            "An evidence-oriented research report containing findings, assumptions, "
            "source requirements, competitors, customer insights, and open questions."
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

