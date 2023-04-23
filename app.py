import customtkinter as ctk
from password_target import PasswordTarget
from data_handler import DataHandler
from password_generator import PasswordGenerator
from error_toplevel import ErrorToplevel
from update_requirements import UpdateTargetRequirements


class App:
    """
    The main class for the application.

    params
    ------
    width: int
    height: int
    password_generator: PasswordGenerator
    datahandler: DataHandler
    result: ctk.StringVar

    methods
    -------
    set_up_window_parts(): sets up the window parts
    set_up_labels(): sets up the labels
    set_up_entrys(): sets up the entrys
    set_up_buttons(): sets up the buttons
    pack_window(): packs the window
    generate_password_btn_callback(): callback for the generate password button
    update_requirements_btn_callback(): callback for the update requirements button
    open_error_message(text): open error toplevel
    open_toplevel(toplevel): opens a toplevel window
    update_data_file(): updates data about the password target
    run(): runs the application

    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes the class.

        Args:
            width (int): window width
            height (int): window height
        """
        self.window = ctk.CTk()
        self.width = width
        self.height = height
        self.password_generator = PasswordGenerator()
        self.datahandler = DataHandler()
        self.result = ctk.StringVar()

    def set_up_window_parts(self) -> None:
        """
        Sets up the window parts.
        """
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title("Password Generator")
        self.window.toplevel_window = None
        self.window.frame_1 = ctk.CTkFrame(master=self.window)

        self.set_up_labels()
        self.set_up_entrys()
        self.set_up_buttons()

    def set_up_labels(self) -> None:
        """
        Sets up the labels.
        """
        self.window.title_label = ctk.CTkLabel(
            master=self.window.frame_1,
            justify=ctk.CENTER,
            text="Password Generator",
            font=("font1", 24),
        )
        self.window.result_label = ctk.CTkLabel(
            master=self.window.frame_1,
            justify=ctk.CENTER,
            text="Your Password:",
            font=("font1", 18),
        )

    def set_up_entrys(self) -> None:
        """
        Sets up the entrys.
        """
        self.window.password_target_entry = ctk.CTkEntry(
            master=self.window.frame_1, placeholder_text="URL or File name", width=250
        )

        self.window.hash_key_entry = ctk.CTkEntry(
            master=self.window.frame_1, placeholder_text="HASH Key", show="*", width=250
        )

        self.window.result_entry = ctk.CTkEntry(
            master=self.window.frame_1,
            placeholder_text="Result Password",
            textvariable=self.result,
            state="disabled",
            width=250,
            font=("font1", 16),
        )

    def set_up_buttons(self) -> None:
        """
        Sets up the buttons.
        """
        self.window.generator_btn = ctk.CTkButton(
            master=self.window.frame_1,
            text="Generate Password",
            command=self.generate_password_btn_callback,
        )

        self.window.update_btn = ctk.CTkButton(
            master=self.window.frame_1,
            text="Update requirements",
            command=self.update_requirements_btn_callback,
        )

    def pack_window(self) -> None:
        """
        Packs the window.
        """
        self.window.frame_1.pack(pady=20, padx=20, fill="both", expand=True)
        self.window.title_label.pack(pady=25, padx=5)
        self.window.password_target_entry.pack(padx=20, pady=10)
        self.window.hash_key_entry.pack(padx=20, pady=10)
        self.window.result_label.pack(pady=5, padx=5)
        self.window.result_entry.pack(padx=20, pady=10)
        self.window.generator_btn.pack(side="top", padx=20, pady=20)
        self.window.update_btn.pack(side="top", padx=20, pady=20)

    def generate_password_btn_callback(self) -> None:
        """
        Callback for the generate password button.
        """
        if not self.window.password_target_entry.get():
            self.open_error_message("no url or file name")
        elif not self.window.hash_key_entry.get():
            self.open_error_message("no hash key")
        elif not self.datahandler.contains(self.window.password_target_entry.get()):
            self.update_data_file(self.window.password_target_entry.get())
        else:
            password_target = self.datahandler.read_target_data_from_file(
                self.window.password_target_entry.get()
            )
            result = self.password_generator.generate_password(
                password_target,
                self.window.hash_key_entry.get(),
            )
            self.result.set(result)

    def update_requirements_btn_callback(self) -> None:
        """
        Callback for the update requirements button.
        """
        if not self.window.password_target_entry.get():
            self.open_error_message("no url or file name")
        self.update_data_file(self.window.password_target_entry.get())

    def open_error_message(self, text: str) -> None:
        """
        Opens an error toplevel

        Args:
            text (str): error message to display
        """
        err = ErrorToplevel(self.window)
        err.window.label.configure(text=text)
        self.open_toplevel(err)
        self.result.set("")

    def open_toplevel(self, toplevel_window: ctk.CTkToplevel) -> None:
        """
        Opens a toplevel window

        Args:
            toplevel_window (ctk.CTkToplevel): toplevel window to open
        """
        if (
            self.window.toplevel_window is None
        ) or not self.window.toplevel_window.window.winfo_exists():
            self.window.toplevel_window = toplevel_window
        else:
            self.window.toplevel_window.window.focus()

    def update_data_file(self, password_target_name: str) -> None:
        """
        Updates data about the password target

        Args:
            password_target_name (str): url or file name of the password target
        """
        if (self.window.toplevel_window is None) or (
            not self.window.toplevel_window.window.winfo_exists()
        ):
            if self.datahandler.contains(password_target_name):
                password_target = self.datahandler.read_target_data_from_file(
                    password_target_name
                )
            else:
                password_target = PasswordTarget(password_target_name)
                self.datahandler.add_password_target(password_target)
            self.window.toplevel_window = UpdateTargetRequirements(
                self.window, password_target, self.datahandler
            )
            self.window.toplevel_window.window.mainloop()
        else:
            self.window.toplevel_window.window.focus()

    def run(self) -> None:
        """
        Runs the application
        """
        self.set_up_window_parts()
        self.pack_window()
        self.window.mainloop()
