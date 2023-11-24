PDF Services

Apple has been annoying in its use of either bugs or features to restrict the use of PDF Services scripts.

Currently (Sonoma OS 14), a python PDF Service will not run if the first line #! uses env. It will work if it calls python directly by a valid pathname, e.g. #!/usr/local/bin/python3.

Ventura and earlier may have sandboxing issues with python running and trying to do things like open file dialogs.
