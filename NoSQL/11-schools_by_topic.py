#!/usr/bin/env python3
"""Module that returns schools having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools that have topic in their topics."""
    return list(mongo_collection.find({"topics": topic}))
