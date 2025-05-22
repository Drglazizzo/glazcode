from flask import Flask, request, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home():
    html = """
    <html>
    <head>
        <title>Onyedikachi Ikenna Onwurah - Portfolio</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background: #f9f9f9;
                color: #333;
            }
            .container {
                max-width: 1000px;
                margin: auto;
                padding: 40px 20px;
            }
            header {
                text-align: center;
                margin-bottom: 40px;
            }
            header img {
                width: 150px;
                height: 150px;
                object-fit: cover;
                border-radius: 50%;
                border: 4px solid #3498db;
            }
            h1, h2 {
                color: #2c3e50;
            }
            .section {
                background: white;
                padding: 20px;
                margin-bottom: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.05);
                transition: transform 0.3s ease;
            }
            .section:hover {
                transform: translateY(-5px);
            }
            ul {
                padding-left: 20px;
            }
            a {
                color: #3498db;
                text-decoration: none;
            }
            form input, form textarea, form button {
                display: block;
                width: 100%;
                margin-top: 10px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            form button {
                background: #3498db;
                color: white;
                cursor: pointer;
                border: none;
            }
            .cert-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 20px;
            }
            .cert-card {
                border: 1px solid #ddd;
                border-radius: 10px;
                overflow: hidden;
                transition: transform 0.3s ease;
                background: white;
            }
            .cert-card:hover {
                transform: scale(1.02);
            }
            .cert-card img {
                width: 100%;
                height: auto;
            }
            .cert-card h4 {
                padding: 10px;
                margin: 0;
                font-size: 16px;
                background: #3498db;
                color: white;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- HEADER -->
            <header>
                <img src="/static/profile.jpg" alt="Profile Picture">
                <h1>👋 Hi, I'm Onyedikachi Ikenna Onwurah</h1>
                <p><strong>Pharmacist and Data Scientist</strong> specializing in Precision Medicine, Machine Learning and Deep Learning.</p>
                <p>
                    <a href="https://linkedin.com/in/onyedikachi-ikenna-onwurah ">LinkedIn</a> | 
                    <a href="https://x.com/drglazcode ">Twitter</a> |
                    <a href="https://www.facebook.com/onwurah.onyedikachi/ ">Facebook</a> |
                    <a href="https://github.com/Drglazizzo ">GitHub</a> | 
                    <a href="mailto:drglazcode@outlook.com">drglazcode@outlook.com</a> | 
                    <a href="mailto:drglazcode@gmail.com">drglazcode@gmail.com</a>
                </p>
            </header>

            <!-- ABOUT ME -->
            <div class="section">
                <h2>🧠 About Me</h2>
                <p>
                    Dynamic pharmacist with 10 years of experience and a passion for leveraging data science to transform healthcare.
                    Currently pursuing a Master's in Data Science specializing in Precision Medicine at the University of Macau.
                    Expert in data analysis, machine learning, and computer vision — proficient in Python, R, SQL, MongoDB and more.
                    Committed to applying interdisciplinary knowledge to improve patient outcomes and drive innovation in healthcare.
                </p>
            </div>

            <!-- CORE COMPETENCIES -->
            <div class="section">
                <h2>🎯 Core Competencies</h2>
                <ul>
                    <li>Data Analysis & Visualization</li>
                    <li>Machine Learning & AI</li>
                    <li>Web Scraping</li>
                    <li>Precision Medicine</li>
                    <li>Statistical Modeling</li>
                    <li>Team Leadership</li>
                    <li>Process Optimization</li>
                    <li>Project Management</li>
                    <li>Healthcare Informatics</li>
                    <li>Pharmacology & Drug Development</li>
                </ul>
            </div>

            <!-- KEY ACHIEVEMENTS -->
            <div class="section">
                <h2>🏆 Key Achievements</h2>
                <ul>
                    <li>Recognized for outstanding performance in patient care, leading to a 20% increase in satisfaction scores</li>
                    <li>Designed a data analysis project that reduced medication errors by 50%</li>
                    <li>Awarded Health Service Award of Gratitude for community health education contributions</li>
                    <li>Achieved top 10% ranking in Kaggle Titanic competition</li>
                    <li>Best Serving Intern at Enugu State University Teaching Hospital, Dec 2015</li>
                </ul>
            </div>

            <!-- EDUCATION -->
            <div class="section">
                <h2>🎓 Education</h2>
                <ul>
                    <li><strong>Master's in Data Science (Precision Medicine)</strong>, University of Macau (2024–Present)</li>
                    <li><strong>Bachelor of Pharmacy</strong>, University of Nigeria (Distinction)</li>
                    <li><strong>West African Senior School Certificate</strong>, Saint Teresa’s College, Nsukka (Distinction)</li>
                </ul>
            </div>

            <!-- CERTIFICATIONS SECTION -->
            <div class="section">
                <h2>📜 Certifications</h2>
                <div class="cert-grid">
                    <a href="/static/Certs/Advanced_Data_Mining_projects_with_R.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/Advanced_Data_Mining_projects_with_R.pdf" alt="Advanced_Data_Mining_Projects_with_R">
                            <h4>Advanced_Data_Mining_with_R</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/Advanced_SQL_Programming.pdf" target="_blank">
            <div class="cert-card">
                <img src="/static/Certs/Advanced_SQL_Programming.pdf" alt="Advanced_SQL_Programming">
                <h4>Advanced_SQL_Programming</h4>
            </div>
                    </a>
                    
                    <a href="/static/Certs/AFFILIATE_MARKETER.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/AFFILIATE_MARKETER.pdf" alt="Affiliate_Marketer">
                            <h4>Affiliate_Marketer</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/AI_AND_APPLICATIONS.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/AI_AND_APPLICATIONS.pdf" alt="AI_AND_APPLICATIONS">
                            <h4>AI_AND_APPLICATIONS</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/App_creation_with_Flutter_and_Dart.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/App_creation_with_Flutter_and_Dart.pdf" alt="App_creation_with_Flutter_and_Dart">
                            <h4>App_creation_with_Flutter_and_Dart</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/BUSINESS_ANALSYT.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/BUSINESS_ANALSYT.pdf" alt="BUSINESS_ANALSYT">
                            <h4>BUSINESS_ANALSYT</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/CLOUD_COMPUTING.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/CLOUD_COMPUTING.pdf" alt="CLOUD_COMPUTING">
                            <h4>CLOUD_COMPUTING</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/Data_Analysis_with_R.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/Data_Analysis_with_R.pdf" alt="Data_Analysis_with_R">
                            <h4>Data_Analysis_with_R</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/DATA_MANAGEMENT_AND_ANALYSIS_CRA.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/DATA_MANAGEMENT_AND_ANALYSIS_CRA.pdf" alt="DATA_MANAGEMENT_AND_ANALYSIS_CRA">
                            <h4>DATA_MANAGEMENT_AND_ANALYSIS_CRA</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/DATA_MANAGEMENT_AND_ANALYSIS.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/DATA_MANAGEMENT_AND_ANALYSIS.pdf" alt="DATA_MANAGEMENT_AND_ANALYSIS">
                            <h4>DATA_MANAGEMENT_AND_ANALYSIS</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/DATA_MINING.ML.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/DATA_MINING.ML.pdf" alt="DATA_MINING.ML">
                            <h4>DATA_MINING.ML</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/DEEP_LEARNING.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/DEEP_LEARNING.pdf" alt="DEEP_LEARNING">
                            <h4>DEEP_LEARNING</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/DEVOPS.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/DEVOPS.pdf" alt="DevOps">
                            <h4>DevOps</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/DIGITAL_LEADERSHIP.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/DIGITAL_LEADERSHIP.pdf" alt="DIGITAL_LEADERSHIP">
                            <h4>DIGITAL_LEADERSHIP</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/DIGITAL_LITERACY.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/DIGITAL_LITERACY.pdf" alt="DIGITAL_LITERACY">
                            <h4>DIGITAL_LITERACY</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/Java_deep_learning.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/Java_deep_learning.pdf" alt="Java_deep_learning">
                            <h4>Java_deep_learning</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/MACHINE_LEARNER.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/MACHINE_LEARNER.pdf" alt="MACHINE_LEARNER">
                            <h4>MACHINE_LEARNER</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/Machine_Learning_and_Deep_with_R.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/Machine_Learning_and_Deep_with_R.pdf" alt="Machine_Learning_and_Deep_with_R">
                            <h4>Machine_Learning_and_Deep_with_R</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/MongoDB.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/MongoDB.pdf" alt="MongoDB Certification">
                            <h4>MongoDB</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/ONYEDIKACHI_ONWURAH_Python.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/ONYEDIKACHI_ONWURAH_Python.pdf" alt="ONYEDIKACHI_ONWURAH_Python">
                            <h4>ONYEDIKACHI_ONWURAH_Python</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/Real_world_python_deep_learning.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/Real_world_python_deep_learning.pdf" alt="Real_world_python_deep_learning">
                            <h4>Real_world_python_deep_learning</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/SQL_aggregate_functions_fundamentals.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/SQL_aggregate_functions_fundamentals.pdf" alt="SQL_aggregate_functions_fundamentals">
                            <h4>SQL_aggregate_functions_fundamentals</h4>
                        </div>
                    </a>
                    
                    <a href="/static/Certs/WEBSITE_UIUX_DESIGNER.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/WEBSITE_UIUX_DESIGNER.pdf" alt="WEBSITE_UIUX_DESIGNER">
                            <h4>WEBSITE_UIUX_DESIGNER</h4>
                            
                    <a href="/static/Certs/BCG_internship_completion_certificate.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/BCG_internship_completion_certificate.pdf" alt="BCG_internship_completion_certificate">
                            <h4>BCG_internship_completion_certificate</h4>
                            
                    <a href="/static/Certs/British_Airways_Data_Science_Internship.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/British_Airways_Data_Science_Internship.pdf" alt="British_Airways_Data_Science_Internship">
                            <h4>British_Airways_Data_Science_Internship</h4>
                            
                    <a href="/static/Certs/PYTHON_PROGRAMMER1.pdf" target="_blank">
                        <div class="cert-card">
                            <img src="/static/Certs/PYTHON_PROGRAMMER1.pdf" alt="PYTHON_PROGRAMMER1">
                            <h4PYTHON_PROGRAMMER1</h4>
                        </div>
                    </a>
                </div>
            </div>

            <!-- DOWNLOAD CV -->
            <div class="section">
                <h2>📄 Download My CV</h2>
                <p>
                    <a href="/static/MY_CURRICULUM_VITAE.pdf" download>
                        <button style="padding: 10px 20px; font-size: 16px; background: #2ecc71; color: white; border: none; border-radius: 5px; cursor: pointer;">
                            📥 Download My CV
                        </button>
                    </a>
                </p>
            </div>

            <!-- CONTACT -->
            <div class="section">
                <h2>📧 Contact Me</h2>
                <p>If you'd like to send me an email, fill out the form below — your email app will open automatically.</p>
                <form onsubmit="sendEmail(event)">
                    <label>Your Name:</label>
                    <input type="text" id="name">
                    <label>Your Email:</label>
                    <input type="email" id="email">
                    <label>Message:</label>
                    <textarea id="message"></textarea>
                    <button type="submit">📩 Send Message</button>
                </form>
            </div>

            <script>
                function sendEmail(event) {
                    event.preventDefault();
                    var name = document.getElementById("name").value;
                    var email = document.getElementById("email").value;
                    var message = document.getElementById("message").value;

                    var mailtoLink = "mailto:drglazcode@outlook.com" +
                                     "?subject=" + encodeURIComponent("New Message from " + name) +
                                     "&body=" + encodeURIComponent("From: " + email + "\\n\\n" + message);

                    window.location.href = mailtoLink;
                }
            </script>
        </div>
    </body>
    </html>
    """
    return html

# Serve static files
@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug=True)