#!/usr/bin/python3
"""Generate personalized invitation files from a template."""
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

PLACEHOLDERS = ["name", "event_title", "event_date", "event_location"]


def generate_invitations(template, attendees):
    """Create output_X.txt files from template for each attendee."""
    if not isinstance(template, str):
        logging.error("Invalid input: template should be a string, got %s",
                      type(template).__name__)
        return
    if not isinstance(attendees, list) or \
            not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees should be a list of "
                      "dictionaries, got %s", type(attendees).__name__)
        return

    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in PLACEHOLDERS:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        try:
            with open(filename, "w") as file:
                file.write(content)
        except OSError as e:
            logging.error("Could not write %s: %s", filename, e)
