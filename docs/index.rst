
Installation
=============


To use `minecraftstatus <https://minecraftstatus.readthedocs.io/en/latest/>`_, install it using `pip <https://pypi.org/project/pip/>`_

.. code-block::
   :linenos:

   (.venv) $ pip install minecraftstatus

or install it from the `github repo <https://github.com/Infernum1/minecraftstatus>`_ using `git <https://git-scm.com>`_ with the following command

.. code-block::
   :linenos:

   (.venv) $ pip install -U git+https://github.com/Infernum1/minecraftstatus

Documentation
=============

.. automodule:: minecraftstatus
    :members:
    :exclude-members: achievement, splash_text, get_server_card
    :undoc-members:
    :show-inheritance:

    .. autofunction:: minecraftstatus.client.MCStatus.achievement

        **How an achievement 'card' would look like:**
         
         .. image:: example_achievement.png
                :width: 640px
                :height: 128px

    .. autofunction:: minecraftstatus.client.MCStatus.splash_text

        **How a splash text 'card' would look like:**
         
         .. image:: example_splash_text.png
                :width: 768px
                :height: 432px
    
    .. autofunction:: minecraftstatus.client.MCStatus.get_server_card

        **How a server 'card' would look like:**
         
         .. image:: example_server_card.png
                :width: 768px
                :height: 140px

.. toctree::
   :maxdepth: 10
   :caption: Contents:
