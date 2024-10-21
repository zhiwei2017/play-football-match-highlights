play football match highlights
==============================

..
    GitHub Actions
    ~~~~~~~~~~~~~~

    You can find all the configuration files of GitHub Actions in ``.github/workflows`` folder.

    Content
    :::::::

    +-------------+----------------------------------------------+--------------------------------------------------+-----------------------------+-----------------------------------------------------------+
    | Config File |          Steps                               |                Trigger Rules                     | Requisite CI/CD Variables   | CI/CD Variables description                               |
    +=============+==============================================+==================================================+=============================+===========================================================+
    |             | mypy check                                   |                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | flake8 check                                 | + **Pushes** to *master/develop* branches        |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    | test.yml    | bandit check                                 | + **Pull Requests** to *master/develop* branches |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | test with python 3.8 (Ubuntu/Mac OS/Windows) |                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | test with python 3.9 (Ubuntu/Mac OS/Windows) |                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | test with python 3.10 (Ubuntu/Mac OS/Windows)|                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | test with python 3.11 (Ubuntu/Mac OS/Windows)|                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | test with python 3.12 (Ubuntu/Mac OS/Windows)|                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | twine check the built package                |                                                  |                             |                                                           |
    +-------------+----------------------------------------------+--------------------------------------------------+-----------------------------+-----------------------------------------------------------+
    |             |                                              |                                                  |                             | Token for uploading package to official PyPi. If you're   |
    |             |                                              |                                                  | POETRY_PYPI_TOKEN_PYPI      | using a private artifactory, please use the variables     |
    |             |                                              |                                                  |                             | `PACKAGE_INDEX_REPOSITORY_URL`, `PACKAGE_INDEX_USERNAME`, |
    |             |                                              |                                                  |                             | and `PACKAGE_INDEX_PASSWORD` instead.                     |
    |             |                                              |                                                  +-----------------------------+-----------------------------------------------------------+
    |             |                                              |                                                  | PACKAGE_INDEX_REPOSITORY_URL| URL of Private package index.                             |
    | release.yml | deploy to PyPi                               | **Pushes** to tags matching *vXX.XX.XX*          +-----------------------------+-----------------------------------------------------------+
    |             |                                              |                                                  | PACKAGE_INDEX_USERNAME      | Username of Private package index.                        |
    |             |                                              |                                                  +-----------------------------+-----------------------------------------------------------+
    |             |                                              |                                                  | PACKAGE_INDEX_PASSWORD      | Password of Private package index.                        |
    +-------------+----------------------------------------------+--------------------------------------------------+-----------------------------+-----------------------------------------------------------+
    | sphinx.yml  | deploy GitHub pages                          | **Pushes** to *master* branch                    |                             |                                                           |
    +-------------+----------------------------------------------+--------------------------------------------------+-----------------------------+-----------------------------------------------------------+

    **Note**:

    + Before publishing the GitHub pages of your project for the first time, please manually create the branch **gh-pages** via::

        $ git checkout master
        $ git checkout -b gh-pages
        $ git push origin gh-pages

    Setup Steps
    :::::::::::

    1. Go to **Settings**.
    2. Click **Secrets** section.
    3. Click **New repository secret** button.
    4. Input the name and value of a CI/CD variable.

    
    Makefile
    ++++++++

    .. list-table::
       :header-rows: 1

       * - Command
         - Description
       * - clean
         - Remove autogenerated folders and artifacts.
       * - clean-pyc
         - Remove python artifacts.
       * - clean-build
         - Remove build artifacts.
       * - bandit
         - Run `bandit`_ security analysis.
       * - mypy
         - Run `mypy`_ type checking.
       * - flake8
         - Run `flake8`_ linting.
       * - install
         - Install all the dependencies and the package itself.
       * - test
         - Run tests and generate coverage report.
       * - build
         - Build wheel package.
       * - publish
         - Publish the built wheel package.

Introduction
------------
Play football match highlights without ads.

User Guide
----------

Requirements
++++++++++++

Optionally this toll uses Chrome browser and the Chrome Extension [Native HLS Playback](https://chromewebstore.google.com/detail/native-hls-playback/emnphkkblegpebimobpbekeedfgemhof?pli=1)
for playing the extracted m3u8 play list. If you want to use this feature, please install Chrome browser
and its extension [Native HLS Playback](https://chromewebstore.google.com/detail/native-hls-playback/emnphkkblegpebimobpbekeedfgemhof?pli=1) firstly.

How to Install
++++++++++++++

Stable release
``````````````

To install play football match highlights, run this command in your terminal:

.. code-block:: console

    $ pip install play_football_match_highlights

or

.. code-block:: console

    $ poetry self add play_football_match_highlights

This is the preferred method to install play football match highlights, as it will always install the most recent stable release.


From sources
````````````

The sources for play football match highlights can be downloaded from the `Github repo <https://github.com/zhiwei2017/play-football-match-highlights>`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone https://github.com/zhiwei2017/play-football-match-highlights.git

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ pip install .

or

.. code-block:: console

    $ poetry install

How to Use
++++++++++

To use play football match highlights in Chrome::

    $ play_match_highlights --with-chrome

To use it just for getting the url for the football match highlight, please use::

    $ play_match_highlights

Maintainers
-----------

..
    TODO: List here the people responsible for the development and maintaining of this project.
    Format: **Name** - *Role/Responsibility* - Email

* **Zhiwei Zhang** - *Maintainer* - `zhiwei2017@gmail.com <mailto:zhiwei2017@gmail.com?subject=[GitHub]play%20football%20match%20highlights>`_