BGPView API
-----------
- Original Author: Sefa Eyeoglu
- Original Repo: https://gitlab.com/Scrumplex/pyqis

--------
The original repo was archived, I cloned / forked the project into github 
and will continue to add functionality.
--------

API client for BGPView.io API

# Usage
An example use is provided in [examples/](examples)
```python
from bgpview import BGPView

viewer = BGPView()
asn_info = viewer.get_asn(1299)
asn_prefixes = viewer.get_asn_prefixes(1299)

# find the origin of a prefix
prefix_info = viewer.get_prefix("2607:3900::/32")

```


# License
This project is licensed under the terms of the GNU General Public License 3.0. Read the full license text [here](LICENSE)
