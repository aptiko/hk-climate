=========================
Source for hk-climate.org
=========================

These are the source files for http://hk-climate.org/.

Compiling
=========

How to compile them after cloning the repository:

1. Install ``make``, ``rest2web``, and the LESS compiler.  In Debian,
   ``apt-get install make rest2web node-less``.

2. In the top level working directory, get the bootstrap source files:
   ``git submodule init; git submodule update``.
   
3. Decide the output location and create a symbolic link to it. The
   compiled files will be placed in the ``output`` subdirectory of the
   top level working directory. However, simply pointing your web
   browser at, say, file:///home/username/hk-climate/output won't work
   properly for various reasons. You need to make the files accessible
   through http, and they must be at the top level directory of the http
   server. What I do in my local machine, where I have default Debian
   apache installation, is ``chown -R $USER /var/www/html; ln -s
   /var/www/html/output``.

4. ``make``

Repository description
======================

Directory ``bootstrap`` is for cloning bootstrap into it, as a git
submodule; it is being used by the LESS stylesheet, which makes a few
modifications to the default bootstrap theme. The LESS stylesheet is in
the ``less`` directory.

Directory ``input`` contains the input files, i.e. the texts in each
language, and the images.

Directory ``preinput`` contains spreadsheets and other stuff that was
manually used in order to produce some of the images in ``input``. It is
there mainly for archival purposes and is not being used by the build
system.

Directory ``other`` is a half-finished attempt to compile the entire
text into a single PDF resembling a paper.

Meta
====

For authorship, copyright, etc., see the "about" page of the web site,
or the source file that produces it, ``input/en/about.txt``.
