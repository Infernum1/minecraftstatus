
Installation
=============


To use `minecraftstatus <https://minecraftstatus.readthedocs.io/en/stable/>`_, install it using `pip <https://pypi.org/project/pip/>`_

.. code-block::
   :linenos:

   (.venv) $ pip install minecraftstatus

or install it from the `github repo <https://github.com/Infernum1/minecraftstatus>`_ using `git <https://git-scm.com>`_ with the following command

.. code-block::
   :linenos:

   (.venv) $ pip install -U git+https://github.com/Infernum1/minecraftstatus

Examples
========
An example of the `get_server <https://minecraftstatus.readthedocs.io/en/stable/#minecraftstatus.MCStatus>`_ feature

.. code-block::
   :linenos:

    import asyncio
    import minecraftstatus

    client = minecraftstatus.MCStatus()


    async def main(ip_address: str):
        server = await client.get_server(ip_address)
        print(server.motd)
        print(server.max_players)
        print(server.max_players)
        print(server.version_info)  # and many more attributes!


    if __name__ == "__main__":
        asyncio.run(main("mc.hypixel.net"))


or the `get_server_card <https://minecraftstatus.readthedocs.io/en/stable/#minecraftstatus.client.MCStatus.get_server_card>`_ feature

.. code-block::
   :linenos:

    import asyncio
    import minecraftstatus

    client = minecraftstatus.MCStatus()


    async def main(ip_address: str):
        image = await client.get_server_card(ip_address, custom_server_name="An Awesome Minecraft Server")
        print(await image.getvalue())


    if __name__ == "__main__":
        asyncio.run(main("mc.hypixel.net"))


Take a look at all the examples on the `github <https://github.com/Infernum1/minecraftstatus/tree/stable/examples>`_

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
