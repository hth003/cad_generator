from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
from crewai_tools import PDFSearchTool, SerperDevTool, ScrapeWebsiteTool
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

# Create a PDF knowledge source
openscad_knowledge = PDFKnowledgeSource(
    file_paths=["OpenSCAD_Tutorial.pdf", "OpenSCAD_Manual.pdf", "OpenSCAD_CheatSheet.pdf"]
)

# Initialize the tool and add content
manual_search_tool = PDFSearchTool(pdf='knowledge/OpenSCAD_Manual.pdf')
tutorial_search_tool = PDFSearchTool(pdf='knowledge/OpenSCAD_Tutorial.pdf')

from cad_generator.tools.custom_tool import OpenSCADValidationTool

@CrewBase
class CadGenerator():
    """CadGenerator crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def cad_system_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['cad_system_designer'], # type: ignore[index]
            tools=[SerperDevTool()], # type: ignore[index]
            memory=False,
            verbose=True
        )

    @agent
    def openscad_code_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['openscad_code_engineer'], # type: ignore[index]
            memory=False,
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def cad_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['cad_design_task'], # type: ignore[index]
        )

    @task
    def openscad_scripting_task(self) -> Task:
        return Task(
            config=self.tasks_config['openscad_scripting_task'],
            tools=[SerperDevTool(), ScrapeWebsiteTool(), manual_search_tool, tutorial_search_tool], # type: ignore[index]
            output_file='openscad_script.scad'
        )

    @task
    def debug_openscad_task(self) -> Task:
        return Task(
            config=self.tasks_config['debug_openscad_task'],
            tools=[OpenSCADValidationTool()],
            output_file='openscad_script.scad'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CadGenerator crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            knowledge_sources=[openscad_knowledge],
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
