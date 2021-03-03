##################################################################
# Usage
##################################################################
if __name__ == "__main__":
  from process import Finder, format_result
  from simulate_data import df_disease, df_biomarker

  # Setence to process
  nltk_sentence = 'very hard angiocarcoma diagnosed 3BHS1'

  # Set up search engine
  finder = Finder(df_disease, df_biomarker)

  # Process and loop through results
  for d, m in finder.process(nltk_sentence):
      format_result(d, m)
