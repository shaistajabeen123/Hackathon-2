"""
Unit tests for the domain models of the Console Todo App.
"""
import unittest
from datetime import datetime
from todo_app.domain.models import TodoItem, TodoList
from todo_app.domain.exceptions import EmptyTitleError


class TestTodoItem(unittest.TestCase):
    """Test cases for the TodoItem class."""
    
    def test_create_todo_item_with_valid_title(self):
        """Test creating a TodoItem with a valid title."""
        title = "Buy groceries"
        item = TodoItem(title)
        
        self.assertEqual(item.title, title)
        self.assertFalse(item.completed)
        self.assertIsNotNone(item.id)
        self.assertIsInstance(item.created_at, datetime)
    
    def test_create_todo_item_with_empty_title_raises_error(self):
        """Test that creating a TodoItem with an empty title raises an error."""
        with self.assertRaises(ValueError):
            TodoItem("")
        
        with self.assertRaises(ValueError):
            TodoItem("   ")  # Only whitespace
    
    def test_mark_complete_sets_completed_to_true(self):
        """Test that mark_complete sets the completed property to True."""
        item = TodoItem("Test item")
        self.assertFalse(item.completed)
        
        item.mark_complete()
        self.assertTrue(item.completed)
    
    def test_mark_incomplete_sets_completed_to_false(self):
        """Test that mark_incomplete sets the completed property to False."""
        item = TodoItem("Test item")
        item.mark_complete()  # First mark as complete
        self.assertTrue(item.completed)
        
        item.mark_incomplete()
        self.assertFalse(item.completed)
    
    def test_update_title_changes_title(self):
        """Test that update_title changes the title."""
        item = TodoItem("Old title")
        self.assertEqual(item.title, "Old title")
        
        new_title = "New title"
        item.update_title(new_title)
        self.assertEqual(item.title, new_title)
    
    def test_update_title_with_empty_title_raises_error(self):
        """Test that updating with an empty title raises an error."""
        item = TodoItem("Old title")
        
        with self.assertRaises(ValueError):
            item.update_title("")
        
        with self.assertRaises(ValueError):
            item.update_title("   ")  # Only whitespace
    
    def test_to_dict_returns_correct_format(self):
        """Test that to_dict returns the correct format."""
        title = "Test item"
        item = TodoItem(title)
        
        item_dict = item.to_dict()
        
        self.assertEqual(item_dict["id"], item.id)
        self.assertEqual(item_dict["title"], title)
        self.assertEqual(item_dict["completed"], False)
        self.assertEqual(item_dict["created_at"], item.created_at.isoformat())


class TestTodoList(unittest.TestCase):
    """Test cases for the TodoList class."""
    
    def setUp(self):
        """Set up a fresh TodoList for each test."""
        self.todo_list = TodoList()
    
    def test_add_item_creates_new_item(self):
        """Test that add_item creates a new item and returns its ID."""
        title = "Buy groceries"
        item_id = self.todo_list.add_item(title)
        
        self.assertIsNotNone(item_id)
        self.assertIn(item_id, self.todo_list.items)
        
        item = self.todo_list.items[item_id]
        self.assertEqual(item.title, title)
        self.assertFalse(item.completed)
    
    def test_get_all_items_returns_all_items(self):
        """Test that get_all_items returns all items in the list."""
        # Add a few items
        id1 = self.todo_list.add_item("Item 1")
        id2 = self.todo_list.add_item("Item 2")
        
        items = self.todo_list.get_all_items()
        
        self.assertEqual(len(items), 2)
        titles = [item.title for item in items]
        self.assertIn("Item 1", titles)
        self.assertIn("Item 2", titles)
    
    def test_get_item_returns_specific_item(self):
        """Test that get_item returns a specific item by ID."""
        original_id = self.todo_list.add_item("Test item")
        
        retrieved_item = self.todo_list.get_item(original_id)
        
        self.assertIsNotNone(retrieved_item)
        self.assertEqual(retrieved_item.title, "Test item")
        self.assertEqual(retrieved_item.id, original_id)
    
    def test_get_item_returns_none_for_nonexistent_id(self):
        """Test that get_item returns None for a nonexistent ID."""
        nonexistent_id = "nonexistent-id"
        retrieved_item = self.todo_list.get_item(nonexistent_id)
        
        self.assertIsNone(retrieved_item)
    
    def test_update_item_updates_title(self):
        """Test that update_item updates the title of an existing item."""
        item_id = self.todo_list.add_item("Old title")
        
        success = self.todo_list.update_item(item_id, "New title")
        
        self.assertTrue(success)
        updated_item = self.todo_list.get_item(item_id)
        self.assertEqual(updated_item.title, "New title")
    
    def test_update_item_returns_false_for_nonexistent_item(self):
        """Test that update_item returns False for a nonexistent item."""
        success = self.todo_list.update_item("nonexistent-id", "New title")
        
        self.assertFalse(success)
    
    def test_delete_item_removes_item_from_list(self):
        """Test that delete_item removes an item from the list."""
        item_id = self.todo_list.add_item("Test item")
        
        success = self.todo_list.delete_item(item_id)
        
        self.assertTrue(success)
        self.assertNotIn(item_id, self.todo_list.items)
    
    def test_delete_item_returns_false_for_nonexistent_item(self):
        """Test that delete_item returns False for a nonexistent item."""
        success = self.todo_list.delete_item("nonexistent-id")
        
        self.assertFalse(success)
    
    def test_mark_complete_marks_item_as_complete(self):
        """Test that mark_complete marks an item as complete."""
        item_id = self.todo_list.add_item("Test item")
        
        success = self.todo_list.mark_complete(item_id)
        
        self.assertTrue(success)
        item = self.todo_list.get_item(item_id)
        self.assertTrue(item.completed)
    
    def test_mark_complete_returns_false_for_nonexistent_item(self):
        """Test that mark_complete returns False for a nonexistent item."""
        success = self.todo_list.mark_complete("nonexistent-id")
        
        self.assertFalse(success)
    
    def test_mark_incomplete_marks_item_as_incomplete(self):
        """Test that mark_incomplete marks an item as incomplete."""
        item_id = self.todo_list.add_item("Test item")
        self.todo_list.mark_complete(item_id)  # First mark as complete
        self.assertTrue(self.todo_list.get_item(item_id).completed)
        
        success = self.todo_list.mark_incomplete(item_id)
        
        self.assertTrue(success)
        item = self.todo_list.get_item(item_id)
        self.assertFalse(item.completed)
    
    def test_mark_incomplete_returns_false_for_nonexistent_item(self):
        """Test that mark_incomplete returns False for a nonexistent item."""
        success = self.todo_list.mark_incomplete("nonexistent-id")
        
        self.assertFalse(success)


if __name__ == '__main__':
    unittest.main()