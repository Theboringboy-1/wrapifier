@echo off


set /p ask=Would you like to install dependencies? (y/n): 

IF %ask% EQU y (
    set install=1
    echo Attempting Installation ...
) else (
    @echo off
    echo Cancelling...
    timeout /t 1 >nul
)

IF "%install%"=="1" (
    @echo off
    echo [LOGS:] Fetching requirements file ...
    timeout /t 2 >nul

    if exist "%~dp0..\requirements.txt" (
        echo [LOGS:] File Fetched ...
        echo [EXECUTING:] Using pip ...

        for /f "delims=" %%A in (%~dp0..\requirements.txt) do (
            echo [INSTALLING:] %%A ...

            pip install %%A >nul 2>&1

            if errorlevel 1 (
                echo [ERROR:] Failed to install %%A ...
            ) else (
                echo [SUCCESS:] %%A installed successfully ...
            )

            echo [FINAL:] Process Completed for %%A
        )
    ) else (
        echo [ERROR:] File not found ...
    )
)


