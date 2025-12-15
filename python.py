<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Yash Gupta Resume</title>
  <meta name="description" content="Yash Gupta — Software Developer | AI & Java Enthusiast" />
  <style>
    /* Black-themed left-panel resume (pixel-perfect, fixed left photo panel) */
    :root{
      --bg:#000000; --panel:#060608; --card:#071017; --muted:#9aa7c6; --accent:#7c5cff; --accent-2:#00d4ff; --glow:rgba(124,92,255,0.14);
      --glass: rgba(255,255,255,0.03);
      --maxw:1200px; --radius:16px; --ff: Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Arial;
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{margin:0;font-family:var(--ff);background:var(--bg);color:#e6eef8}

    .wrap{min-height:100vh;display:grid;grid-template-columns:420px 1fr;gap:28px;align-items:stretch;max-width:1200px;margin:28px auto;padding:20px}
    @media (max-width:980px){.wrap{grid-template-columns:1fr;padding:16px}}

    /* LEFT PANEL */
    .left{position:relative;border-radius:18px;overflow:hidden;background:linear-gradient(180deg, rgba(255,255,255,0.01), transparent);border:1px solid rgba(255,255,255,0.03);box-shadow:0 40px 90px rgba(2,6,23,0.7)}
    .left .bg-shape{position:absolute;inset:0;background:radial-gradient(400px 140px at 10% 20%, rgba(0,212,255,0.03), transparent 10%), radial-gradient(300px 100px at 80% 80%, rgba(124,92,255,0.03), transparent 10%)}
    .photo-wrap{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding:46px 28px;height:100%}
    .avatar{width:240px;height:240px;border-radius:50%;overflow:hidden;border:8px solid rgba(255,255,255,0.02);box-shadow:0 30px 80px rgba(0,0,0,0.6), 0 0 50px var(--glow);background:linear-gradient(90deg,var(--accent),var(--accent-2));display:flex;align-items:center;justify-content:center}
    .avatar img{width:100%;height:100%;object-fit:cover;display:block}
    .name{margin-top:20px;font-size:22px;font-weight:800;text-align:center}
    .role{margin-top:6px;color:var(--muted);text-align:center}

    .left .info{margin-top:18px;padding:0 10px;text-align:center}
    .left .meta{display:flex;flex-direction:column;gap:10px;align-items:center;margin-top:12px}
    .pill{background:rgba(255,255,255,0.02);padding:10px 14px;border-radius:999px;color:var(--muted);font-weight:700}

    .socials{display:flex;gap:10px;justify-content:center;margin-top:18px}
    .socials a{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:linear-gradient(90deg,var(--accent),var(--accent-2));color:#071126;text-decoration:none;font-weight:800}

    /* RIGHT CONTENT */
    .right{overflow:auto;padding:28px}
    .card{background:linear-gradient(180deg, rgba(255,255,255,0.01), transparent);padding:20px;border-radius:12px;border:1px solid rgba(255,255,255,0.03);margin-bottom:18px}
    h2{margin:0 0 8px 0;color:#dbe9ff}
    p.lead{margin:0;color:var(--muted)}

    /* Skills bars */
    .skills{display:grid;grid-template-columns:1fr 1fr;gap:14px}
    .skill{padding:14px;border-radius:12px;background:rgba(255,255,255,0.005);border:1px solid rgba(255,255,255,0.02)}
    .skill .title{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;font-weight:700}
    .bar{height:12px;background:rgba(255,255,255,0.02);border-radius:999px;overflow:hidden}
    .fill{height:100%;border-radius:999px;background:linear-gradient(90deg,var(--accent),var(--accent-2));box-shadow:0 6px 24px rgba(0,212,255,0.06);transition:width .8s cubic-bezier(.2,.9,.2,1)}

    /* Experience list */
    .exp-item{padding:16px;border-radius:12px;background:linear-gradient(180deg, rgba(255,255,255,0.005), rgba(255,255,255,0.003));margin-bottom:12px;border:1px solid rgba(255,255,255,0.01)}
    .exp-meta{font-size:0.94rem;color:var(--muted);margin-top:8px}

    /* Projects */
    .projects{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
    @media (max-width:720px){.projects{grid-template-columns:1fr}}
    .project{padding:14px;border-radius:12px;background:rgba(255,255,255,0.005);border:1px solid rgba(255,255,255,0.01)}
    .project a{color:var(--accent-2);font-weight:700}

    /* Certificates carousel */
    .carousel{display:flex;gap:12px;overflow-x:auto;padding-bottom:8px}
    .cert{min-width:220px;border-radius:12px;background:rgba(255,255,255,0.01);padding:12px;border:1px solid rgba(255,255,255,0.02)}
    .cert img{width:100%;height:130px;object-fit:cover;border-radius:8px}

    /* Contact */
    .contact-form{display:grid;gap:10px}
    input,textarea{width:100%;padding:12px;border-radius:8px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:#e6eef8}
    .btn{padding:10px 14px;border-radius:10px;border:0;font-weight:700;cursor:pointer}
    .btn.primary{background:linear-gradient(90deg,var(--accent),var(--accent-2));color:#071126}

    footer{color:var(--muted);text-align:center;margin-top:18px}

    /* helpers */
    .muted{color:var(--muted)}
    .right h3{margin-top:0}

    /* ensure left panel fixed on tall pages */
    @media(min-width:981px){
      .wrap{align-items:flex-start}
      .left{position:sticky;top:28px;height:calc(100vh - 56px)}
    }
  </style>
</head>
<body>
  <div class="wrap">
    <!-- LEFT PANEL (fixed photo + small details) -->
    <aside class="left" aria-label="Profile panel">
      <div class="bg-shape" aria-hidden="true"></div>
      <div class="photo-wrap">
        <div class="avatar" role="img" aria-label="Yash Gupta photo">
          <img src="photo2.jpg" alt="Yash Gupta">
        </div>
        <div class="name">Yash Gupta</div>
        <div class="role">Software Developer | AI & Java Enthusiast</div>

        <div class="info">
          <div class="meta">
            <div class="pill">SRM IST • B.Tech CSE (2024–28)</div>
            <div class="pill">Chennai, Tamil Nadu</div>
            <div class="pill">+91 7895864944</div>
          </div>

          <div class="socials" style="margin-top:18px">
            <a href="https://github.com/YASHRNN13" target="_blank">GH</a>
            <a href="https://www.linkedin.com/in/yash-gupta-aba124327/" target="_blank">in</a>
            <a href="https://www.hackerrank.com/profile/yg7565" target="_blank">HR</a>
            <a href="https://leetcode.com/u/YASHRNN13/" target="_blank">LC</a>
          </div>
        </div>
      </div>
    </aside>

    <!-- RIGHT CONTENT (scrollable) -->
    <main class="right" id="main">
      <section class="card">
        <h2>Resume</h2>
        <p class="lead">A passionate software developer with strong skills in Python, Java, AI-based systems, and GUI development. Focused on building intelligent applications and continuously improving technical expertise.</p>
      </section>

      <section class="card">
        <h3>Skills</h3>
        <div class="skills" aria-hidden="false">
          <div class="skill">
            <div class="title"><span>Python</span><span>90%</span></div>
            <div class="bar"><div class="fill" style="width:90%"></div></div>
          </div>
          <div class="skill">
            <div class="title"><span>Java</span><span>86%</span></div>
            <div class="bar"><div class="fill" style="width:86%"></div></div>
          </div>
          <div class="skill">
            <div class="title"><span>C / C++</span><span>75%</span></div>
            <div class="bar"><div class="fill" style="width:75%"></div></div>
          </div>
          <div class="skill">
            <div class="title"><span>HTML</span><span>72%</span></div>
            <div class="bar"><div class="fill" style="width:72%"></div></div>
          </div>
          <div class="skill">
            <div class="title"><span>Java Swing</span><span>70%</span></div>
            <div class="bar"><div class="fill" style="width:70%"></div></div>
          </div>
          <div class="skill">
            <div class="title"><span>Pandas & NumPy</span><span>68%</span></div>
            <div class="bar"><div class="fill" style="width:68%"></div></div>
          </div>
        </div>
      </section>

      <section class="card">
        <h3>Experience & Leadership</h3>
        <div class="exp-item">
          <div style="display:flex;justify-content:space-between"><strong>Committee Member & Event Coordinator — Aaruush, SRM IST</strong><span class="muted">July 2025 – Present</span></div>
          <div class="exp-meta muted">Planned and coordinated departmental and inter-college events. Led ideation, implementation, team communication, and on-ground operations.</div>
        </div>
      </section>

      <section class="card">
        <h3>Projects</h3>
        <div class="projects">
          <div class="project">
            <strong>Offline Pincode Checker</strong>
            <p class="muted">Python + CSV — Local lookup tool to search by post office name or pincode number. Fast, offline, and user-friendly.</p>
            <div class="muted" style="margin-top:8px"><a href="https://github.com/YASHRNN13/Pincode-Checker" target="_blank">GitHub</a></div>
          </div>

          <div class="project">
            <strong>Web Translator AI (Group)</strong>
            <p class="muted">Java Swing + VOSK + Google Translate — Desktop translator with speech recognition and multilingual text translation. MySQL used for persistence.</p>
            <div class="muted" style="margin-top:8px"><a href="https://github.com/vansh-gg/WEB-TRANSLATOR" target="_blank">GitHub</a></div>
          </div>

          <div class="project">
            <strong>Additional Learning Projects</strong>
            <p class="muted">Multiple small-scale projects in Python and Java. Full portfolio on GitHub.</p>
            <div class="muted" style="margin-top:8px"><a href="https://github.com/YASHRNN13" target="_blank">github.com/YASHRNN13</a></div>
          </div>

          <div class="project">
            <strong>Ongoing Experiments</strong>
            <p class="muted">Exploring AI code helpers and automation scripts. Happy to collaborate on internships and real projects.</p>
          </div>
        </div>
      </section>

      <section class="card">
        <h3>Certificates</h3>
        <div class="carousel" aria-label="Certificates carousel">
          <a class="cert" href="Programming In Java.pdf" target="_blank"><img src="/mnt/data/Programming In Java.pdf.png" alt="NPTEL certificate"><small class="muted">NPTEL — Programming in Java (Jul–Oct 2025)</small></a>
          <a class="cert" href="YA_YRF0L_The_2025 (1).pdf" target="_blank"><img src="/mnt/data/YA_YRF0L_The_2025 (1).pdf.png" alt="Aaruush"><small class="muted">Aaruush — The Art of Fortune (27 Jun 2025)</small></a>
          <a class="cert" href="Certificate (1).pdf" target="_blank"><img src="/mnt/data/Certificate (1).pdf.png" alt="AI workshop"><small class="muted">Python Using AI Workshop (19 Oct 2025)</small></a>
        </div>
      </section>

      <section class="card">
        <h3>Interests</h3>
        <p class="muted">Coding, Music, Playing & Watching Cricket, Researching Political History & Indian Mythology (Mahabharata, Ramayana).</p>
      </section>

      <section class="card">
        <h3>Contact</h3>
        <form class="contact-form" onsubmit="event.preventDefault();submitContact()">
          <input id="cname" placeholder="Your name" required />
          <input id="cemail" placeholder="Your email" required />
          <textarea id="cmsg" rows="4" placeholder="Message" required></textarea>
          <div style="display:flex;justify-content:flex-end"><button class="btn primary" type="submit">Send</button></div>
        </form>
      </section>

      <footer><small class="muted">© Yash Gupta — Built for portfolio & hiring. Place <code>photo2.jpg</code> and certificate thumbnails in the same folder for everything to load locally.</small></footer>
    </main>
  </div>

  <script>
    // small interactivity
    document.querySelectorAll('.fill').forEach(el=>{el.style.width = el.style.width});
    function submitContact(){
      const n=document.getElementById('cname').value.trim();
      const e=document.getElementById('cemail').value.trim();
      const m=document.getElementById('cmsg').value.trim();
      if(!n||!e||!m){alert('Please fill all fields');return}
      alert('Thanks '+n+"! This demo site doesn't have a backend — message not sent.");
      document.getElementById('cname').value='';document.getElementById('cemail').value='';document.getElementById('cmsg').value='';
    }
  </script>
</body>
</html>
