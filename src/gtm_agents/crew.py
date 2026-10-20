from crewai import Crew, Process

from .agents import (
    create_analyst_agent,
    create_head_planner,
    create_research_agent,
    create_strategy_agent,
)
from .tasks import create_tasks


def create_gtm_crew() -> Crew:
    head_planner = create_head_planner()
    research_agent = create_research_agent()
    analyst_agent = create_analyst_agent()
    strategy_agent = create_strategy_agent()

    tasks = create_tasks(
        head_planner=head_planner,
        research_agent=research_agent,
        analyst_agent=analyst_agent,
        strategy_agent=strategy_agent,
    )

    return Crew(
        agents=[
            head_planner,
            research_agent,
            analyst_agent,
            strategy_agent,
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

