# Basic Text Components

As mentioned on the main page, there are many basic text components, 
but these text components can be recreated in markdown. 
Below are bullets with the st component and their equivalent in markdown:

* `st.title` - `#`
* `st.header` - `##`
* `st.subheader` - `###`
* `st.write`
* `st.caption`
* `st.code` - `
* `st.text` - 4 spaces at start of line
* `st.latex` - ❌
* `st.divider` - *****

It is in my opinion unless you need small text objects, fill in large text areas with markdown. 
I create an assets folder that I can put images and markdown files in.
Then I load in the markdown as a string in Python and pass that as an `st.markdown()`

    with file(markdown_path_str, "r") as f:
        markdown_str = f.read()
    st.markdown(markdown_str)

The LaTeX functionality above is for displaying mathematical equations, 
it is not suggested to create a who Streamlit document in LaTeX.

## HTML

If you want to write your own HTML, you can do that with `st.html()`. This does not work with iFrames or Javascript.
If you would like to run your own iframes, use this:

    import streamlit.components.v1 as components

    components.iframe("https://url.target", height=800)

For a component with custom Javascript, you will need to create your own [Streamlit Component](https://docs.streamlit.io/develop/api-reference/custom-components). 