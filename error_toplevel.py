import customtkinter as ctk


class ErrorToplevel:
    """
    ErrorToplevel is a toplevel window that displays an error message.

    Parameters
    ----------
    master : ctk.CTk

    Attributes
    ----------
    window : ctk.CTkToplevel

    Methods
    -------

    ok_callback : ctk.CTkButton
    set_up_error_toplevel : ctk.CTkToplevel

    Examples
    --------
    >>> import customtkinter as ctk
    >>> root = ctk.CTk()
    >>> ErrorToplevel(root)
    >>> root.mainloop()

    """

    def __init__(self, master: ctk.CTk) -> None:
        """
        Parameters
        ----------
        master (ctk.CTk): master ctk widget
        """
        self.window = ctk.CTkToplevel(master)
        self._set_up_error_toplevel()

    def _ok_callback(self) -> None:
        """
        Callback for OK button, destroy the window.
        """
        self.window.destroy()

    def _set_up_error_toplevel(self) -> None:
        """
        Set up the error toplevel window.
        """
        self.window.geometry("300x150")
        self.window.title("Error")
        self.window.label = ctk.CTkLabel(self.window, text="Error")
        self.window.label.pack(padx=20, pady=20)
        self.window.ok_btn = ctk.CTkButton(
            master=self.window, text="OK", command=self._ok_callback
        )
        self.window.ok_btn.pack(side="top", padx=10, pady=5)
