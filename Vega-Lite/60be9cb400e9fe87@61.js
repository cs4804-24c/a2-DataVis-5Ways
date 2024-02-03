import define1 from "./26670360aa6f343b@209.js";
import define2 from "./a2166040e5fb39a6@229.js";

function _1(md){return(
md`# Visualization using vega-lite`
)}

function _peng(FileAttachment){return(
FileAttachment("penglings.csv").csv()
)}

function _5(vl,peng){return(
vl.markCircle().data(peng).encode(
  vl.x().field("flipper_length_mm").type("quantitative").scale({domain: [170,240]}),
  vl.y().field("body_mass_g").type("quantitative").scale({domain: [2000,6500]}),
  vl.color().field('species'),
  vl.size({field: "bill_length_mm", type: "quantitative", scale: {domain: [30,55]}})
).render()
)}

export default function define(runtime, observer) {
  const main = runtime.module();
  function toString() { return this.url; }
  const fileAttachments = new Map([
    ["penglings.csv", {url: new URL("./files/c03abd7fe3565fb7a4e33fe54471a658f6b5ec8ae42075b5643e394f1d0c5a04bf58ac1da442931489aba6f26f6d45c4a2bc3ab05bb35b79a0fa41b32a7f4833.csv", import.meta.url), mimeType: "text/csv", toString}]
  ]);
  main.builtin("FileAttachment", runtime.fileAttachments(name => fileAttachments.get(name)));
  main.variable(observer()).define(["md"], _1);
  const child1 = runtime.module(define1);
  main.import("vl", child1);
  const child2 = runtime.module(define2);
  main.import("printTable", child2);
  main.variable(observer("peng")).define("peng", ["FileAttachment"], _peng);
  main.variable(observer()).define(["vl","peng"], _5);
  return main;
}
