"""Interfaces for the presentation layer."""

from abc import ABC, abstractmethod

from business.world.interfaces import IGameWorld

class IComponentHolder(ABC):
    """A user interface handler, which controls all component"""

    @abstractmethod
    def update(self, display: "IDisplay") -> None:
        """Updates all the data for the buttons on screen"""

    @abstractmethod
    def add_component(self, component: "IUIComponent") -> None:
        """Adds a component to the user screen"""

    @abstractmethod
    def remove_component(self, component: "IUIComponent") -> None:
        """Removes a component from the screen"""

    @property
    @abstractmethod
    def components(self):
        """All the components in the menu"""

class IDisplay(ABC):
    """Interface for displaying the game world."""

    @property
    @abstractmethod
    def screen(self):
        """The pygame screen in which everything is rendered"""

    @abstractmethod
    def load_world(self, world: IGameWorld):
        """Load the world into the display.

        Args:
            world (IGameWorld): The game world to be displayed.
        """

    @abstractmethod
    def render_frame(self):
        """Render the current frame."""

    @abstractmethod
    def get_menu(self, name: str) -> "IMenu":
        """Gets one of the screen menus
        
            Return:
                IMenu: A screen menu
        """


class IInputHandler(ABC):
    """Interface for handling user input."""

    @abstractmethod
    def add_event(self, event):
        """Adds an event to the queue for this frame"""

    @abstractmethod
    def reset_events(self):
        """Resets all the queued events"""

    @abstractmethod
    def process_input(self):
        """Process the input from the user."""

class IRootComponent(ABC):
    """Root for all component types"""

    @abstractmethod
    def update(self, display: "IDisplay"):
        """Update the frame on the screen"""

    @abstractmethod
    def set_active(self, state: bool):
        """CHanges the state of the UI Component to either be drawn or not on screen"""

    @property
    @abstractmethod
    def active(self) -> bool:
        """Whether or not the ui component is to be drawn on screen
        
            Returns:
                bool: The state of the UI
        """

class IUIComponent(IRootComponent):
    """A component of the user's visual interface"""

    @property
    @abstractmethod
    def rect(self):
        """The ui component's rect
        
            Returns:
                pygame.Rect: The rect hitbox containing the ui component
        """

    @property
    @abstractmethod
    def original_properties(self):
        """The original properties of the UI object before any edits are made"""

    @property
    @abstractmethod
    def color(self):
        """The color of the UI component, by default white
        
            Returns:
                tuple[int, int, int]: The color in RGB
        """

    @abstractmethod
    def change_color(self, new_color: tuple[int, int, int]):
        """Change the color of the UI button to a new one

            Args:
                new_color: tuple[int, int, int]
        """

    @abstractmethod
    def draw(self):
        """Draw the component on a surface
        
            Returns:
                Surface: the drawn surface
        """

class IDynamicUIComponent(IUIComponent):
    """UI component with position and """

    @abstractmethod
    def move(self, pos):
        """Move the object to a part of the screen"""

    @abstractmethod
    def resize(self, size):
        """Change the size of the UI element"""

    @abstractmethod
    def change_opacity(self, opacity):
        """Change the opacity of the UI element"""

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
    def opacity(self):
        """The opacity of the ui element on screen

            Returns:
                int: The opacity of the element on the screen
        """

class IMenu(IComponentHolder):
    """A general menu for interfaces"""

    @property
    @abstractmethod
    def active(self):
        """Whether or not the menu can be rendered"""

    @property
    @abstractmethod
    def name(self) -> str:
        """The name of the menu

            Returns:
                str: The menu of the menu
        """

    @abstractmethod
    def draw(self):
        """Draws all of the menu's components"""

    @abstractmethod
    def set_active(self, state: bool) -> None:
        """Sets whether or not the menu is active"""

class IClickable(ABC):
    """Can be clicked when the mouse is inside object"""

    @abstractmethod
    def is_clicked(self):
        """Method that runs once the button is clicked"""

class IUserInterfaceHandler(ABC):
    """A general user interface handler"""

    @abstractmethod
    def update(self, display: IDisplay):
        """Update all the screen ui elements"""

    @abstractmethod
    def add_menu(self, menu: IMenu) -> None:
        """Adds a menu to the screen"""

    @abstractmethod
    def remove_menu(self, menu: IMenu) -> None:
        """Adds a menu to the screen"""

    @abstractmethod
    def get_menu(self, name: str) -> IMenu:
        """Gets a saved menu component"""


class IText(IRootComponent):
    """A screen text that can be applied to any part of the screen"""

    @abstractmethod
    def change(self, text: str) -> None:
        """Changes the displayed text"""

    @property
    @abstractmethod
    def text(self) -> str:
        """The text inside the text object"""

class IButton(IDynamicUIComponent, IClickable):
    """A UI button used in menus"""

    @abstractmethod
    def attach_text(self, text: IText):
        """Attach a text to the button"""

    @property
    @abstractmethod
    def hover_time(self):
        """The tick in which the player started hovering over the button
        
            Returns:
                int: ticks
        """

    @abstractmethod
    def is_hovering(self) -> bool:
        """Whether the user is or isn't hovering over the button
        
            Returns:
                bool: being hovered or not
        """

class IDynamicText(IDynamicUIComponent):
    """A text with a background object"""

class IImageComponent(IDynamicUIComponent):
    """A dynamic component that also holds an image"""

    @property
    @abstractmethod
    def image(self):
        """The image attached to the component"""

    @abstractmethod
    def resize_image(self, new_size):
        """Change the size the image covers inside the original frame 
        (by default 90% of the original image size)"""
