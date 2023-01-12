Get the template
To use the tamplate first clone this repository.

git clone https://github.com/pixpack/streamlit-base.git my-streamlit-app
Move into the templates directory.

cd my-streamlit-app
On Github you can also click the Use this template button to automatically create your own repository based on this template.

Create the development environment
Create a virtual environment.

python -m venv .venv

Activate the virtual environment.

On Linux, macOS.

```bash
source .venv/bin/activate
```

On Windows (Powershell).

```bash
.venv/Scripts/Activate.ps1
```

Get the development dependencies.

```bash
python -m pip install --upgrade pip && \
pip install -r requirements-dev.txt
```