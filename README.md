# lpprecision.github.io

# Developer Instructions

This site uses jinja2 to make changing site contents easier.
`jinja2-templates` contains html templates used to build the site.
`configs` contains the editable files to edit content.

## Basic editing

Just edit the files under `config/` and build with the instructions below.
**Edits to the HTML will be overwritten by the site build process!**

Please use the provided conda environment to build the site:

```
conda env create -f environment.yaml
conda activate webdev
```

Build the site with:
`python build_with_jinja2.py`

Run the following to host the site locally to preview:
`./localhost.sh`

**Remember to build, then add all the modified files before you push.**
