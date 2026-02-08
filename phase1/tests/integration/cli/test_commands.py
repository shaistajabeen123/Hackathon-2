"""
Integration tests for the CLI commands of the Console Todo App.
"""
import unittest
from io import StringIO
import sys
from unittest.mock import patch
from todo_app.domain.models import TodoList
from todo_app.application.services import TodoAppService
from todo_app.cli.commands import TodoCommandHandler


class TestAddCommandIntegration(unittest.TestCase):
    """Integration tests for the add command."""
    
    def setUp(self):
        """Set up the application components for each test."""
        self.todo_list = TodoList()
        self.app_service = TodoAppService(self.todo_list)
        self.command_handler = TodoCommandHandler(self.app_service)
    
    def test_add_command_successfully_adds_todo(self):
        """Test that the add command successfully adds a todo."""
        title = "Buy groceries"
        args = ["add", title]
        
        result = self.command_handler.handle_add(args)
        
        # Check that the result indicates success
        self.assertIn("Todo added successfully", result)
        self.assertIn("ID:", result)
        
        # Check that the todo was actually added to the list
        todos = self.todo_list.get_all_items()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].title, title)
        self.assertFalse(todos[0].completed)
    
    def test_add_command_with_empty_title_fails(self):
        """Test that the add command fails with an empty title."""
        args = ["add", ""]
        
        result = self.command_handler.handle_add(args)
        
        # Check that the result indicates an error
        self.assertIn("Error:", result)
        self.assertIn("cannot be empty", result)
        
        # Check that no todos were added
        todos = self.todo_list.get_all_items()
        self.assertEqual(len(todos), 0)
    
    def test_add_command_with_whitespace_only_title_fails(self):
        """Test that the add command fails with a whitespace-only title."""
        args = ["add", "   "]
        
        result = self.command_handler.handle_add(args)
        
        # Check that the result indicates an error
        self.assertIn("Error:", result)
        self.assertIn("cannot be empty", result)
        
        # Check that no todos were added
        todos = self.todo_list.get_all_items()
        self.assertEqual(len(todos), 0)


    def test_add_command_with_whitespace_only_title_fails(self):
        """Test that the add command fails with a whitespace-only title."""
        args = ["add", "   "]

        result = self.command_handler.handle_add(args)

        # Check that the result indicates an error
        self.assertIn("Error:", result)
        self.assertIn("cannot be empty", result)

        # Check that no todos were added
        todos = self.todo_list.get_all_items()
        self.assertEqual(len(todos), 0)


class TestListCommandIntegration(unittest.TestCase):
    """Integration tests for the list/view command."""

    def setUp(self):
        """Set up the application components for each test."""
        self.todo_list = TodoList()
        self.app_service = TodoAppService(self.todo_list)
        self.command_handler = TodoCommandHandler(self.app_service)

    def test_list_command_shows_empty_list_message_when_no_todos(self):
        """Test that the list command shows an empty list message when there are no todos."""
        result = self.command_handler.handle_list()

        self.assertIn("Your todo list is empty", result)

    def test_list_command_shows_all_todos_with_status(self):
        """Test that the list command shows all todos with their status."""
        # Add a few todos
        id1 = self.todo_list.add_item("First todo")
        id2 = self.todo_list.add_item("Second todo")

        # Mark one as complete
        self.todo_list.mark_complete(id1)

        result = self.command_handler.handle_list()

        # Check that the result contains the expected information
        self.assertIn("Todos:", result)
        self.assertIn("[x]", result)  # Completed item
        self.assertIn("[ ]", result)  # Incomplete item
        self.assertIn("First todo", result)
        self.assertIn("Second todo", result)
        self.assertIn(id1, result)
        self.assertIn(id2, result)


class TestCompleteCommandIntegration(unittest.TestCase):
    """Integration tests for the complete/incomplete commands."""

    def setUp(self):
        """Set up the application components for each test."""
        self.todo_list = TodoList()
        self.app_service = TodoAppService(self.todo_list)
        self.command_handler = TodoCommandHandler(self.app_service)

        # Add a test todo
        self.item_id = self.todo_list.add_item("Test todo")

    def test_complete_command_marks_todo_as_complete(self):
        """Test that the complete command marks a todo as complete."""
        args = ["complete", self.item_id]

        result = self.command_handler.handle_complete(args)

        # Check that the result indicates success
        self.assertIn("Todo marked as complete", result)

        # Check that the todo is actually marked as complete
        item = self.todo_list.get_item(self.item_id)
        self.assertTrue(item.completed)

    def test_incomplete_command_marks_todo_as_incomplete(self):
        """Test that the incomplete command marks a todo as incomplete."""
        # First mark as complete
        self.todo_list.mark_complete(self.item_id)
        self.assertTrue(self.todo_list.get_item(self.item_id).completed)

        args = ["incomplete", self.item_id]

        result = self.command_handler.handle_incomplete(args)

        # Check that the result indicates success
        self.assertIn("Todo marked as incomplete", result)

        # Check that the todo is actually marked as incomplete
        item = self.todo_list.get_item(self.item_id)
        self.assertFalse(item.completed)

    def test_complete_command_fails_for_nonexistent_todo(self):
        """Test that the complete command fails for a nonexistent todo."""
        args = ["complete", "nonexistent-id"]

        result = self.command_handler.handle_complete(args)

        # Check that the result indicates an error
        self.assertIn("Error:", result)
        self.assertIn("not found", result)

    def test_incomplete_command_fails_for_nonexistent_todo(self):
        """Test that the incomplete command fails for a nonexistent todo."""
        args = ["incomplete", "nonexistent-id"]

        result = self.command_handler.handle_incomplete(args)

        # Check that the result indicates an error
        self.assertIn("Error:", result)
        self.assertIn("not found", result)


class TestUpdateCommandIntegration(unittest.TestCase):
    """Integration tests for the update command."""

    def setUp(self):
        """Set up the application components for each test."""
        self.todo_list = TodoList()
        self.app_service = TodoAppService(self.todo_list)
        self.command_handler = TodoCommandHandler(self.app_service)

        # Add a test todo
        self.item_id = self.todo_list.add_item("Original title")

    def test_update_command_updates_todo_title(self):
        """Test that the update command updates a todo's title."""
        new_title = "Updated title"
        args = ["update", self.item_id, new_title]

        result = self.command_handler.handle_update(args)

        # Check that the result indicates success
        self.assertIn("Todo updated successfully", result)

        # Check that the todo's title is actually updated
        item = self.todo_list.get_item(self.item_id)
        self.assertEqual(item.title, new_title)

    def test_update_command_fails_for_nonexistent_todo(self):
        """Test that the update command fails for a nonexistent todo."""
        args = ["update", "nonexistent-id", "New title"]

        result = self.command_handler.handle_update(args)

        # Check that the result indicates an error
        self.assertIn("Error:", result)
        self.assertIn("not found", result)

    def test_update_command_fails_for_empty_new_title(self):
        """Test that the update command fails for an empty new title."""
        args = ["update", self.item_id, ""]

        result = self.command_handler.handle_update(args)

        # Check that the result indicates an error
        self.assertIn("Error:", result)
        self.assertIn("cannot be empty", result)

        # Check that the original title is preserved
        item = self.todo_list.get_item(self.item_id)
        self.assertEqual(item.title, "Original title")


class TestDeleteCommandIntegration(unittest.TestCase):
    """Integration tests for the delete command."""

    def setUp(self):
        """Set up the application components for each test."""
        self.todo_list = TodoList()
        self.app_service = TodoAppService(self.todo_list)
        self.command_handler = TodoCommandHandler(self.app_service)

        # Add a test todo
        self.item_id = self.todo_list.add_item("Test todo to delete")

    def test_delete_command_removes_todo_from_list(self):
        """Test that the delete command removes a todo from the list."""
        args = ["delete", self.item_id]

        result = self.command_handler.handle_delete(args)

        # Check that the result indicates success
        self.assertIn("Todo deleted successfully", result)

        # Check that the todo is actually removed from the list
        items = self.todo_list.get_all_items()
        self.assertEqual(len(items), 0)

        # Check that the todo cannot be retrieved anymore
        item = self.todo_list.get_item(self.item_id)
        self.assertIsNone(item)

    def test_delete_command_fails_for_nonexistent_todo(self):
        """Test that the delete command fails for a nonexistent todo."""
        args = ["delete", "nonexistent-id"]

        result = self.command_handler.handle_delete(args)

        # Check that the result indicates an error
        self.assertIn("Error:", result)
        self.assertIn("not found", result)


if __name__ == '__main__':
    unittest.main()