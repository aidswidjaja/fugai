# Fugai
## an open source alternative to Steam Overlay, Discord Overlay and TeamSpeak (Overwolf) Overlay

The Fugai application is going to serve as a codebase for a few other projects. While it works as a standalone app, it may be buggy, unmaintained, and additional features might be implemented elsewhere. While using this repo directly isn't recommended for end user use, it should work out fine.

As of 27 June 2020, project development continues at an extremely slow pace. It's like, barely being kept alive. The idea isn't to have a working product so soon, but rather just to have a codebase I can work on for things and other dependents by the time those projects are ready :D

### Roadmap:
- [Bug] Fix window flags
- Hide/Show keybinds
- Save window geometry
- Import other local packages (like Ashbadger)

***

### Cross-platform and open-source overlay for rapid communication and information with minimal performance impact for macOS and Windows and _maybe_ Linux.

- Get rapid access to utilities and interfaces without impacting your computer's performance
- Customise Fugai's window positioning, background, and settings to your own liking
- Get access to Steam, Chrome, Teamspeak and Discord without Alt-Tabbing out of your game
- EULA friendly - no hacks involved
- Available for macOS, Windows, and Linux window managers that support compositing
- Designed for single-monitor setups but works on multi-monitor setups too (with a few bumps tho)
- Free and open-source - fork/modify the software and contribute code on [GitHub](https://github.com/aidswidjaja/fugai)

***

## Design Principles

- Lightweight - there shouldn't be a noticeable impact when gaming or running other resource-heavy programs
- Easy to use - a user shouldn't have to be experienced in Python, PySide, window managers, X11, DirectX, calculus, integrals, polynomials, whatever science you use to build rockets, etc. to get started with Fugai
- Do what works, not what's right - no solution is overkill. That being said...
- Modular - code and end user UI should be flexible and versatile. Don't dig yourself into a hole with your own code
- Functional not aesthetic - Fluent Design animations look cool and everything but the codebase for Fugai is designed to be functional first - we're leaving pretty UI up to any forkers who want to use Fugai as a base for their own projects. Feel free to submit pull requests of any aesthetic improvements though - but as an end user don't expect it. 

## Dependencies

If compiling from source (as opposed to binaries) the most current list of dependencies can be found below (most can be installed via pip):
- [Python 3.8.3rc1 and all its included packages (e.g sys, datetime)](https://www.python.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyQtWebEngine](https://pypi.org/project/PyQtWebEngine/)
- [qtmodern](https://github.com/gmarull/qtmodern)

That's a lot of 🥧!

## Why is there a random screen shot of your desktop in the Git repo I cloned?

idek I must have accidentally put it in but I'll keep it there as a nice easter egg lol.

## 

***

## License

Except where otherwise stated:

```
2020 (c) aidswidjaja and other contributors.
MIT License (see LICENSE.md)
```

100% free and open source under the MIT License.

Thanks to the numerous people who've shared their knowledge online (you're credited as comments in the code). 

Stack Exchange licensing info:
- https://meta.stackexchange.com/questions/271080/the-mit-license-clarity-on-using-code-on-stack-overflow-and-stack-exchange