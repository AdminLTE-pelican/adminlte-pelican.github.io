# AdminLTE-pelican

This is a simplified pelican port of the bootstrap theme [AdminLTE](https://github.com/ColorlibHQ/AdminLTE/). Currently under construction and looking for contributors and collaborators.

A demo of the template is available [here](https://adminlte-pelican.github.io/).

## Features
* Bootstrap support for layout, components, etc.
* Responsive, mobile ready layout.
* Dark mode with toggle switch supported.
* Mathjax support available
* Pygments support available for syntax highlighting
* Flickr gallery support as custom template.
* Custom search using google available.
* Custom 404 page template.

# TODO

[ ] Implement breadcrumb support for pages/subpages.
[ ] Implement google analytics support.
[ ] Implement comment support for disqus, graphcomments.
[ ] Implement pagination support.

# THEME SETTINGS

Syntax highlighting style can be specified using:

    PYGMENTS_STYLE = 'nord'

Available styles can be chosen from the list avilable [here](https://pygments.org/styles/).

The number of recent posts to display on the right sidebar can be set using:

    RECENT_POST_COUNT = 2



## Flickr support
The theme contains a `gallery.html` template which can be specified in any specific post/page to ddisplay a flickr album. The template relies on [nanogallery2](https://nanogallery2.nanostudio.org/) and a typical application is shown [here](https://adminlte-pelican.github.io/photography/).

# License

[AdminLTE](https://adminlte.io/docs/3.2/index.html) is an open source project that is licensed under the [MIT license](https://opensource.org/licenses/MIT). This allows you to do pretty much anything you want as long as you include the copyright in “all copies or substantial portions of the Software.” Attribution is not required (though very much appreciated).

## What You Are Allowed To Do With AdminLTE

* Use in commercial projects.
* Use in personal/private projects.
* Modify and change the work.
* Distribute the code.
* Sublicense: incorporate the work into something that has a more restrictive license.

## What You Are Not Allowed To Do With AdminLTE

* The work is provided “as is”. You may not hold the author liable.

## What You Must Do When Using AdminLTE

* Include the license notice in all copies of the work.
* Include the copyright notice in all copies of the work. This applies to everything except the notice in the footer of the HTML example pages.


