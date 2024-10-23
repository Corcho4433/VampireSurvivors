"""Interfaces for the presentation layer."""

from abc import ABC, abstractmethod

from business.world.interfaces import IGameWorld

class IUserInterfaceHandler(ABC):
    """A user interface handler, which controls all component"""

    @abstractmethod
    def add_component(self) -> None:
        """Adds a component to the user screen"""

    @abstractmethod
    def remove_component(self) -> None:
        """Removes a component from the screen"""

class IDisplay(ABC):
    """Interface for displaying the game world."""

    @abstractmethod
    def load_world(self, world: IGameWorld):
        """Load the world into the display.

        Args:
            world (IGameWorld): The game world to be displayed.
        """

    @abstractmethod
    def render_frame(self):
        """Render the current frame."""


class IInputHandler(ABC):
    """Interface for handling user input."""

    @abstractmethod
    def process_input(self):
        """Process the input from the user."""

class IUIComponent(ABC):
    """A component of the user's visual interface"""
    
    @abstractmethod
    def update(self):
        """Update the frame on the screen"""


    @abstractmethod
    def set_active(self, state: bool):
        """CHanges the state of the UI Component to either be drawn or not on screen"""


    @property
    @abstractmethod
    def pos(self):
        """The position of the ui element on screen

            Returns:
                Vector2: The position of the element on the screen
        """

    @property
    @abstractmethod
    def size(self):
        """The size of the ui element on screen

            Returns:
                Vector2: The size of the element on the screen
        """

    @property
    @abstractmethod
    def active(self) -> bool:
        """Whether or not the ui component is to be drawn on screen
        
            Returns:
                bool: The state of the UI
        """

class IClickable(ABC):
    """Can be clicked when the mouse is inside object"""

    @abstractmethod
    def clicked(self):
        """Method that runs once the button is clicked"""

class IButton(IUIComponent, IClickable):
    """A UI button used in menus"""