.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
imio.transmogrifier.blueprints
==============================================================================

Groups and deploy all differents blueprints to migrate Imio Plone Site 2.x, 3.x to Plone 4.x. (read import.cfg)

Features
--------

- Can use different blueprints



Examples
--------
    ...
    cardimporter
    TTGoogleMapMarkerToCard
    fix_utf-8
    ...
    
[cardimporter]
blueprint = imio.transmogrifier.cardimporter.cardimporter

[TTGoogleMapMarkerToCard]
blueprint = imio.transmogrifier.cardimporter.TTGoogleMapMarkerToCard

[fix_utf-8]
blueprint = imio.transmogrifier.PloneFormGen.fix_utf-8


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install imio.transmogrifier.blueprints by adding it to your buildout::

    [buildout]

    ...

    eggs =
        imio.transmogrifier.blueprints


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/imio.transmogrifier.blueprints/issues
- Source Code: https://github.com/collective/imio.transmogrifier.blueprints
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
