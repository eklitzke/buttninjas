Imagine that you have a web application that accepts input from users and
renders it somehow. For this web application to be safe and correct the user
input has to be "escaped" before rendering it on the page.

One problem you may have in a large, complex web application is that getting all
of the details with respect to escaping input can be tricky. In particular, if
you double escape HTML input, or escape input that doesn't need escaping, you'll
get funny looking output. For instance, let's say our original input buffer is:

    hello &para;

If we escape this input the output will be like

    hello &amp;para;

Which will end up being rendered to the user as `hello &para;` instead of
`hello ¶` which we desire.

Now if your application is well structured and carefully written you'll know
exactly which strings need to be escaped and which don't, and you won't have
this problem. But applications grow and become complex, and despite good
intentions it can be hard to prevent double escaping.

The buttninja string replacement technique is one mechanism to try to work
around the double-escaping problem. It is an effort to avoid double escaped
ampersands.

## Testing

This project has unit tests, and in fact strives for 100% test coverage. You can
run the unit tests by install [pytest](http://pytest.org/) and then running:

    py.test tests/

## Bugs

Any occurrences of "buttninjas" in the original input buffer will be converted
to ampersands.
