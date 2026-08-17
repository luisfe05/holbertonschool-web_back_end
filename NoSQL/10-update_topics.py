#!/usr/bin/env python3
"""Module that updates the topics of a school document by name."""


def update_topics(mongo_collection, name, topics):
    """Update the topics of all documents matching name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
