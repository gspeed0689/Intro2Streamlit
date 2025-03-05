# Media

Another basic component of websites is media, and Streamlit has many options for that as well. 

## Photo and Images

You can add a photo in your markdown with the `![](https://image.url/path.jpg)` approach in your long texts, 
but remember that this is standard markdown, not a dialect that will support image sizing in the markdown. 

To add an image with custom sizing, you can use `st.image` and pass it an file path, a url, a numpy array, an image bytes object, or a PIL object. 

## Audio and Video

You can also embed an audio or video player with `st.audio` and `st.video`, and similarly you can pass the function a file path, a url, or a bytes object. 
`st.video` can even take a YouTube url! 