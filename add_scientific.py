# Create a ready-to-merge symbols-extra.json with common scientific/math symbols.
import json, os, textwrap, pathlib

symbols = [
  {"e":"°","n":"degree sign","c":"symbols","k":["degree","deg","temperature","angle","arcdegree"],"p":0.86},
  {"e":"℃","n":"degree Celsius sign","c":"symbols","k":["degree celsius","celsius","centigrade","temperature","°C"],"p":0.84},
  {"e":"℉","n":"degree Fahrenheit sign","c":"symbols","k":["degree fahrenheit","fahrenheit","temperature","°F"],"p":0.82},
  {"e":"°C","n":"degree Celsius","c":"symbols","k":["degree celsius","celsius","centigrade","temperature"],"p":0.82},
  {"e":"°F","n":"degree Fahrenheit","c":"symbols","k":["degree fahrenheit","fahrenheit","temperature"],"p":0.80},

  {"e":"∇","n":"nabla","c":"symbols","k":["nabla","del","gradient","vector calculus"],"p":0.78},
  {"e":"∂","n":"partial derivative","c":"symbols","k":["partial","derivative","d/dx","calculus","curly d"],"p":0.78},
  {"e":"Δ","n":"capital delta","c":"symbols","k":["delta","change","difference","increment","triangle"],"p":0.76},
  {"e":"δ","n":"delta","c":"symbols","k":["delta","change","difference","small delta"],"p":0.70},
  {"e":"π","n":"pi","c":"symbols","k":["pi","3.14159","circle","tau/2"],"p":0.88},
  {"e":"τ","n":"tau","c":"symbols","k":["tau","2π","circle"],"p":0.60},
  {"e":"λ","n":"lambda","c":"symbols","k":["lambda","wavelength","eigenvalue"],"p":0.66},
  {"e":"μ","n":"mu (Greek)","c":"symbols","k":["mu","micro","mean"],"p":0.68},
  {"e":"µ","n":"micro sign","c":"symbols","k":["micro","mu","10^-6","prefix"],"p":0.68},
  {"e":"Ω","n":"omega (ohm)","c":"symbols","k":["ohm","resistance","omega"],"p":0.74},
  {"e":"Ω","n":"ohm sign","c":"symbols","k":["ohm","resistance","omega","compatibility"],"p":0.52},

  {"e":"∞","n":"infinity","c":"symbols","k":["infinite","limit","math"],"p":0.82},
  {"e":"≈","n":"approximately equal","c":"symbols","k":["approx","approximately","about equal","almost equal"],"p":0.74},
  {"e":"≠","n":"not equal","c":"symbols","k":["not equal","inequality","≠"],"p":0.82},
  {"e":"≤","n":"less-than or equal","c":"symbols","k":["<= ","le","less or equal","inequality"],"p":0.72},
  {"e":"≥","n":"greater-than or equal","c":"symbols","k":[">=","ge","greater or equal","inequality"],"p":0.72},
  {"e":"±","n":"plus-minus","c":"symbols","k":["plus minus","uncertainty","tolerance"],"p":0.76},
  {"e":"−","n":"minus sign","c":"symbols","k":["minus","negative","en dash minus","math minus"],"p":0.70},
  {"e":"×","n":"multiplication sign","c":"symbols","k":["times","multiply","cross"],"p":0.78},
  {"e":"÷","n":"division sign","c":"symbols","k":["divide","division","obelus"],"p":0.70},
  {"e":"·","n":"middle dot","c":"symbols","k":["dot","center dot","multiply","scalar"],"p":0.56},
  {"e":"⋅","n":"dot operator","c":"symbols","k":["dot","dot operator","multiply","scalar"],"p":0.58},

  {"e":"√","n":"square root","c":"symbols","k":["root","square root","radical"],"p":0.78},
  {"e":"∛","n":"cube root","c":"symbols","k":["root","cube root","radical"],"p":0.60},

  {"e":"∑","n":"summation","c":"symbols","k":["sum","sigma","series"],"p":0.76},
  {"e":"∏","n":"product","c":"symbols","k":["product","capital pi","series"],"p":0.60},
  {"e":"∫","n":"integral","c":"symbols","k":["integral","calculus","area"],"p":0.74},
  {"e":"∮","n":"contour integral","c":"symbols","k":["contour integral","line integral","calculus"],"p":0.52},
  {"e":"∝","n":"proportional to","c":"symbols","k":["proportional","proportional to","varies as"],"p":0.60},

  {"e":"∈","n":"element of","c":"symbols","k":["in","element of","set"],"p":0.58},
  {"e":"∉","n":"not an element of","c":"symbols","k":["not in","not element","set"],"p":0.56},
  {"e":"⊂","n":"subset of","c":"symbols","k":["subset","proper subset","set"],"p":0.56},
  {"e":"⊆","n":"subset of or equal","c":"symbols","k":["subset or equal","subseteq","set"],"p":0.54},
  {"e":"⊃","n":"superset of","c":"symbols","k":["superset","proper superset","set"],"p":0.54},
  {"e":"⊇","n":"superset of or equal","c":"symbols","k":["superset or equal","supseteq","set"],"p":0.52},
  {"e":"∪","n":"union","c":"symbols","k":["union","set union"],"p":0.60},
  {"e":"∩","n":"intersection","c":"symbols","k":["intersection","set intersection"],"p":0.60},

  {"e":"∠","n":"angle","c":"symbols","k":["angle","geometry"],"p":0.52},
  {"e":"⊥","n":"perpendicular","c":"symbols","k":["perpendicular","orthogonal","right angle"],"p":0.60},
  {"e":"∥","n":"parallel","c":"symbols","k":["parallel","lines","||"],"p":0.52},
  {"e":"∘","n":"ring operator","c":"symbols","k":["compose","function composition","circle"],"p":0.44},

  {"e":"′","n":"prime","c":"symbols","k":["prime","minutes","arcminutes","feet"],"p":0.58},
  {"e":"″","n":"double prime","c":"symbols","k":["double prime","seconds","arcseconds","inches"],"p":0.56},
  {"e":"‰","n":"per mille","c":"symbols","k":["permille","per thousand","per mille"],"p":0.40},
  {"e":"‱","n":"basis point","c":"symbols","k":["per ten thousand","basis points","bp"],"p":0.38},

  {"e":"→","n":"right arrow","c":"symbols","k":["arrow","right","maps to","implies"],"p":0.74},
  {"e":"←","n":"left arrow","c":"symbols","k":["arrow","left"],"p":0.60},
  {"e":"↑","n":"up arrow","c":"symbols","k":["arrow","up"],"p":0.60},
  {"e":"↓","n":"down arrow","c":"symbols","k":["arrow","down"],"p":0.60},
  {"e":"↔","n":"left right arrow","c":"symbols","k":["arrow","left right","bidirectional"],"p":0.58},
  {"e":"⇒","n":"implies","c":"symbols","k":["implies","double arrow","then"],"p":0.60},
  {"e":"⇔","n":"if and only if","c":"symbols","k":["iff","equivalence","biconditional","double arrow"],"p":0.60},

  {"e":"Å","n":"angstrom","c":"symbols","k":["angstrom","Ångström","angstrom unit","1e-10 m"],"p":0.50}
]

out = "/symbols-extra.json"
pathlib.Path("").mkdir(parents=True, exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    json.dump(symbols, f, ensure_ascii=False, indent=2)

out
