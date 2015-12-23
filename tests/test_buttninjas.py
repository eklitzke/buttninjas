import pytest

import buttninjas


@pytest.mark.parametrize('inbuf,outbuf',
                         [('', ''),
                          ('foo', 'foo'),
                          ('&', '&amp;'),
                          ('&amp;', '&amp;'),
                          ('&permil;', '&amp;permil;'),
                          ('buttninjas', '&amp;')
                         ])
def test_escape(inbuf, outbuf):
    assert buttninjas.escape_input(inbuf) == outbuf
