#!/usr/bin/env python
# src/lead_scraper/main.py
import sys
from lead_scraper.crew import LeadScraperCrew

def run():
  """
  Run the crew.
  """
  inputs = {
    'topic': 'AI Agents'
  }
  LeadScraperCrew().crew().kickoff(inputs=inputs)
