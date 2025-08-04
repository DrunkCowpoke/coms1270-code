# Trevor Bentley             7-26-2025
# Assignment 5: Ultimate to do list test

# this code uses pytest to vibe check the todo list
# not a requirement but im submitting it with the todo list 

import pytest
from ultimateTODO import checkItem, addItem, deleteItem, moveItem

# ----- Blank slate everytime, yes I googled how to -----

@pytest.fixture

# -------------------------------------------------------------------
# -------------------------- CITATION: ------------------------------
# Source: pytest development team
# Title: Fixtures: Managing test state
# URL: https://docs.pytest.org/en/stable/how-to/fixtures.html
# Accessed: 2025-07-26
#--------------------------------------------------------------------

def fresh_todo():
    return {"backlog": [],"todo": [],"in_progress": [],"in_review": [],"done": []}

# ----- checkItem -----
def test_checkItem_found(fresh_todo):
    fresh_todo["backlog"].append("homework")
    found, key, index = checkItem("homework", fresh_todo)
    assert found is True
    assert key == "backlog"
    assert index == 0

def test_checkItem_not_found(fresh_todo):
    found, key, index = checkItem("write a strongly worded letter to Pearson", fresh_todo)
    assert found is False
    assert key == ""
    assert index == -1

# ----- addItem -----
def test_addItem_success(fresh_todo):
    updated = addItem("feed cat", "todo", fresh_todo)
    assert "feed cat" in updated["todo"]

def test_addItem_duplicate_skips_add(fresh_todo):
    fresh_todo["done"].append("meditate")
    updated = addItem("meditate", "backlog", fresh_todo)
    assert updated["backlog"] == []

# ----- deleteItem -----
def test_deleteItem_exists(fresh_todo):
    fresh_todo["in_progress"].append("dishes")
    found, updated = deleteItem("dishes", fresh_todo)
    assert found is True
    assert "dishes" not in updated["in_progress"]

def test_deleteItem_not_found(fresh_todo):
    found, updated = deleteItem("cry", fresh_todo)
    assert found is False
    for tasks in updated.values():
        assert "cry" not in tasks

# ----- moveItem -----
def test_moveItem_success(fresh_todo):
    fresh_todo["backlog"].append("cram for tomorrow's exam")
    updated = moveItem("cram for tomorrow's exam", "in_progress", fresh_todo)
    assert "cram for tomorrow's exam" in updated["in_progress"]
    assert "cram for tomorrow's exam" not in updated["backlog"]

def test_moveItem_not_found_does_nothing(fresh_todo):
    updated = moveItem("write a strongly worded letter to Pearson", "done", fresh_todo)
    for key in updated:
        assert "write a strongly worded letter to Pearson" not in updated[key]