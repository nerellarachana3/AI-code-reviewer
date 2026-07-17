from google import genai
import gradio as gr

client=genai.Client(api_key="Gemini_API")

def review(code):
  prompt=f"""
  Review the code

  Includes:
  -Summary
  -Bugs
  -Code style
  -Rating out of 10

  code:
  {code}
  """
  response=client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompt
  )
  return response.text
demo=gr.Interface(
    fn=review,
    inputs=gr.Textbox(label="code"),
    outputs="markdown",
    title="AI code Review(gemini)"

)
demo.launch()
