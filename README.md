# IFacets

The package is a helper for integrating [Facets] into [IPython] notebooks.

## Installation

```bash
git clone --recursive https://github.com/IvanUkhov/ifacets.git
make -C ifacets
```


## Usage

```python
import IFacets

IFacets.preamble()
IFacets.overview(data)
IFacets.dive(data)
```

[facets]: https://pair-code.github.io/facets/
[ipython]: https://ipython.org/
