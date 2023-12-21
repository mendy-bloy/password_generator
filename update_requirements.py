import customtkinter as ctk
from password_target import PasswordTarget
from data_handler import DataHandler


class UpdateTargetRequirements:
    """
    This class defines the update target requirements window.


    Attributes
    ----------
    window : ctk.CTkToplevel
    password_target : PasswordTarget
    data_handler : DataHandler
    min_uppers_optionmenu_var : ctk.StringVar
    min_lowers_optionmenu_var : ctk.StringVar
    min_digits_optionmenu_var : ctk.StringVar
    length_optionmenu_var : ctk.StringVar

    Methods
    -------
    define_vars()
    set_up_buttons()
    set_up_optionmenus()
    set_up_toplevel_window()
    submit_btn_callback()
    min_uppers_optionmenu_callback()
    min_lowers_optionmenu_callback()
    min_digits_optionmenu_callback()
    length_optionmenu_callback()

    """

    def __init__(
        self,
        master: ctk.CTk,
        password_target: PasswordTarget,
        data_handler: DataHandler,
    ) -> None:
        self.window = ctk.CTkToplevel(master)
        self.password_target = password_target
        self.data_handler = data_handler
        self.set_up_toplevel_window()

    def define_vars(self) -> None:
        """
        Defines the variables used in the update target requirements window.

        """
        self.min_uppers_optionmenu_var = ctk.StringVar(
            value=self.password_target.min_uppers
        )
        self.min_lowers_optionmenu_var = ctk.StringVar(
            value=self.password_target.min_lowers
        )
        self.min_digits_optionmenu_var = ctk.StringVar(
            value=self.password_target.min_digits
        )
        self.length_optionmenu_var = ctk.StringVar(value=self.password_target.length)

    def set_up_buttons(self) -> None:
        """
        Defines the buttons used in the update target requirements window.

        """
        self.window.submit_btn = ctk.CTkButton(
            master=self.window.frame_1,
            text="Submit",
            command=self.submit_btn_callback,
        )

    def set_up_optionmenus(self) -> None:
        """
        Defines the optionmenus used in the update target requirements window.
        """

        self.window.min_uppers_optionmenu = ctk.CTkOptionMenu(
            master=self.window.frame_1,
            values=[str(_) for _ in range(10)],
            command=self.min_uppers_optionmenu_callback,
            variable=self.min_uppers_optionmenu_var,
            fg_color=("blue", "black"),
        )
        self.window.min_lowers_optionmenu = ctk.CTkOptionMenu(
            master=self.window.frame_1,
            values=[str(_) for _ in range(10)],
            command=self.min_lowers_optionmenu_callback,
            variable=self.min_lowers_optionmenu_var,
            fg_color=("blue", "black"),
        )
        self.window.min_digits_optionmenu = ctk.CTkOptionMenu(
            master=self.window.frame_1,
            values=[str(_) for _ in range(10)],
            command=self.min_digits_optionmenu_callback,
            variable=self.min_digits_optionmenu_var,
            fg_color=("blue", "black"),
        )
        self.window.length_optionmenu = ctk.CTkOptionMenu(
            master=self.window.frame_1,
            command=self.length_optionmenu_callback,
            variable=self.length_optionmenu_var,
            fg_color=("blue", "black"),
        )

    def set_up_labels(self) -> None:
        """
        Defines the labels used in the update target requirements window.
        """

        self.window.label = ctk.CTkLabel(
            self.window.frame_1,
            text="Update URL or file\npassword requirements",
            font=("font1", 20),
        )
        self.window.min_uppers_label = ctk.CTkLabel(
            self.window.frame_1,
            text="Minimum number of\nupper-case letters required:",
            font=("font1", 14),
            text_color="grey91",
        )
        self.window.min_lowers_label = ctk.CTkLabel(
            self.window.frame_1,
            text="Minimum number of\nlower-case letters required:",
            font=("font1", 14),
            text_color="grey91",
        )
        self.window.min_digits_label = ctk.CTkLabel(
            self.window.frame_1,
            text="Minimum number of\nmin_digits required:",
            font=("font1", 14),
            text_color="grey91",
        )
        self.window.length_label = ctk.CTkLabel(
            self.window.frame_1,
            text="Required length\nof password:",
            font=("font1", 14),
            text_color="grey91",
        )
        self.reconfigure_length_optionmenu()

    def min_uppers_optionmenu_callback(self, choice) -> None:
        """
        Callback function for the min_uppers_optionmenu.
        set the minimum number of upper-case letters in the password.

        Args:
            choice (str): optionmenu choice.
        """
        self.password_target.min_uppers = int(choice)
        self.window.min_uppers_optionmenu.configure(fg_color=("grey"))
        self.reconfigure_length_optionmenu()

    def min_lowers_optionmenu_callback(self, choice) -> None:
        """
        Callback function for the min_lowers_optionmenu.
        set the minimum number of lower-case letters in the password.

        Args:
            choice (str): optionmenu choice.
        """
        self.password_target.min_lowers = int(choice)
        self.window.min_lowers_optionmenu.configure(fg_color=("grey"))
        self.reconfigure_length_optionmenu()

    def min_digits_optionmenu_callback(self, choice) -> None:
        """
        Callback function for the min_digits_optionmenu.
        set the minimum number of digits in the password.

        Args:
            choice (str): optionmenu choice.
        """
        self.password_target.min_digits = int(choice)
        self.window.min_digits_optionmenu.configure(fg_color=("grey"))
        self.reconfigure_length_optionmenu()

    def length_optionmenu_callback(self, choice) -> None:
        """
        Callback function for the length_optionmenu.
        set the required length of the password.

        Args:
            choice (str): optionmenu choice.
        """
        self.password_target.length = int(choice)
        self.window.length_optionmenu.configure(fg_color=("grey"))

    def submit_btn_callback(self) -> None:
        """
        Callback function for the submit_btn.
        update the data base with the new password requirements and destroy the window.

        """
        self.data_handler.update_data_file(self.password_target)
        self.window.destroy()

    def compute_minimum_length(self) -> int:
        """
        Computes the minimum length of the password.

        Returns:
            int: minimum length of the password.
        """
        return (
            self.password_target.min_uppers
            + self.password_target.min_lowers
            + self.password_target.min_digits
        )

    def reconfigure_length_optionmenu(self) -> None:
        """
        Reconfigures the length_optionmenu.
        """
        min_len = self.compute_minimum_length()
        if int(self.length_optionmenu_var.get()) < min_len:
            self.length_optionmenu_var.set(min_len)
        self.password_target.length = int(self.window.length_optionmenu.get())
        self.window.length_optionmenu.configure(
            values=[str(_) for _ in range(min_len, 30)],
        )

    def pack_window(self) -> None:
        """
        Packs the window.
        """
        self.window.frame_1.pack(pady=20, padx=20, fill="both", expand=True)
        self.window.label.pack(padx=20, pady=25)
        self.window.min_uppers_label.pack(padx=20, pady=5)
        self.window.min_uppers_optionmenu.pack(padx=20, pady=10)
        self.window.min_lowers_label.pack(padx=20, pady=5)
        self.window.min_lowers_optionmenu.pack(padx=20, pady=10)
        self.window.min_digits_label.pack(padx=20, pady=5)
        self.window.min_digits_optionmenu.pack(padx=20, pady=10)
        self.window.length_label.pack(padx=20, pady=5)
        self.window.length_optionmenu.pack(padx=20, pady=10)
        self.window.submit_btn.pack(side="top", padx=20, pady=50)

    def set_up_toplevel_window(self) -> None:
        """
        Sets up the toplevel window.
        """
        self.window.geometry("400x650")
        self.window.title("Update requirements")
        self.window.frame_1 = ctk.CTkFrame(master=self.window)

        self.define_vars()
        self.set_up_buttons()
        self.set_up_optionmenus()
        self.set_up_labels()
        self.pack_window()
