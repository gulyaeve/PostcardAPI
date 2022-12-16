page_template_1 = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <style>
      @font-face {{
        font-family: 'Bebas';
        src: url(font.ttf);
      }}
      body {{background: #365d6b;}}
      .left, .right, .center {{
        margin: -5px 0;
      }}
      .main {{
        display: table;
        margin: 25px auto;
      }}
      .center.p1 {{
        background: url('center11.png') repeat-x;
        height: 114px;
        min-width: 100px;
      }}
      .center.p2 {{
        background: #365d6b;
        width: 656px;
        min-height: 272px;
        height: auto;
      }}
      .center.p3 {{
        background: url('center13.png') repeat-x;
        height: 115px;
        min-width: 100px;
      }}
      .left.p1 {{
        background: url('left11.png') repeat-y;
        height: 114px;
        width: 302px;
      }}
      .left.p2 {{
        background: url('left12.png') repeat-y;
        width: 302px;
        min-height: 19px;
      }}
      .left.p3 {{
        background: url('left13.png') repeat-y;
        height: 368px;
        width: 302px;
      }}
      .right.p1 {{
        background: url('right11.png') repeat-y;
        width: 371px;
        height: 114px;
      }}
      .right.p2 {{
        background: url('right12.png') repeat-y;
        min-height: 19px;
      }}
      .right.p3 {{
        background: url('right13.png') repeat-y;
        width: 371px;
        height: 359px;
      }}

      .text {{
        max-width: 800px;
        margin: auto;
        color: white;
        font-size: 70px;
        word-wrap: normal;
        font-family: Bebas, Arial;
        text-align: center;
        text-shadow: 0 0 10px #777;
      }}
    </style>
  </head>
  <body>
    <div id="main" class="main">
      <div class="left main" style="float: left;">
        <div class="left p1">
        </div>
        <div id="left-p2" class="left p2">
        </div>
        <div class="left p3">
        </div>
      </div>
      <div id="center-main" class="center main" style="float: left;">
        <div class="center p1">
        </div>
        <div class="center p2">
          <div class="center p2 text-block" style="display:flex; height: 100%;">
            <h1 class="text">{text}</h1>
          </div>
        </div>
        <div class="center p3">
        </div>
      </div>
      <div class="right main" style="float: left;">
        <div class="right p1">
        </div>
        <div id="right-p2" class="right p2">
        </div>
        <div class="right p3">
        </div>
      </div>
    </div>
    <script>
      window.onload = function() {{
         console.log('Start');
         var cen_str = getComputedStyle(document.getElementById("center-main")).height;
         var cenHeight = cen_str.replace(/[a-zа-яё]/gi, '');
         document.getElementById('main').style.height = Number(cenHeight) + 'px';
         document.getElementById('left-p2').style.height = (Number(cenHeight) - 461) + 'px';
         document.getElementById('right-p2').style.height = (Number(cenHeight) - 463) + 'px';
         console.log(Number(cenHeight));
      }};
    </script>
  </body>
</html>

"""
