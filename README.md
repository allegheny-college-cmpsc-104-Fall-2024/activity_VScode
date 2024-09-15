
# Activity 1 - Running Linters with GitHub Actions

## Timeline
<table>
  <thead>
      <td style="text-align:left;">Assigned</td>
      <td style="text-align:left;">Friday 20 September 2024</td>
  </thead>
  <tfoot>
      <td style="text-align:left; color: red;">Deadline</td>
      <td style="text-align:left;">END OF CLASS</td>
  </tfoot>
</table>

![Activity 1](https://github.com/allegheny-college-cmpsc-104-Fall-2024/activity_VScode/blob/main/graphics/github_actions.png)

## Project Goals
- Learn how to use linters for code quality checks.
- Configure an automated linting process with GitHub Actions.
- Gain experience with practical DevOps automation for codebase maintenance.

## Learning Outcomes
These assignment learning outcomes contribute to the following course learning outcomes described in the course syllabus:

1. Describe and explain processes such as software installation or design for a variety of technical and non-technical audiences ranging from inexperienced to expert.
2. Use professional-grade integrated development environments (IDEs), command-line tools, and version control systems to compose, edit, and deploy well-structured, web-ready documents and industry-standard documentation tools.
3. Build automated publishing pipelines to format, check, and ensure both the uniformity and quality of digital documents.

## Instructions
Create a workflow file (.yml) in your repository under the .github/workflows/ directory. Please name it py_lint.yml. (The example code is located on the final slide in the `classDocs/lessons/week4_vscode` directory for your reference.)

## Resources
- Official Visual Studio Code Documentation: https://code.visualstudio.com/docs
- Git Integration with VSCode: https://code.visualstudio.com/docs/editor/versioncontrol

## Deliverables
Please submit your work by pushing it to your GitHub Classroom repository.

## Project Assessment
- Successfully meets the criteria set by GatorGrader.

## Gator Grade
### GatorGrade Checks for Immediate Feedback

To provide immediate feedback on your submissions, we're utilizing GatorGrade. Upon submission, if there's a thick red X, it indicates missing components. This X will turn into a green check mark once your submission is complete. For details on what's missing, click on the red X.

To meet the lab assignment's baseline writing and commit requirements, you can use the department's `GatorGrade` tool. Ensure Python3 is installed on your computer (check with `python --version`). If Python is not installed, please follow these guides:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [Setting Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Installing `GatorGrade`:

- [Install](https://pipx.pypa.io/stable/) [pipx](https://pipx.pypa.io/stable/) if you haven't already (`pip install pipx`).
- Install `GatorGrade` using pipx (`pipx install gatorgrade`).
- Running `GatorGrade`:
 `gatorgrade --config config/gatorgrade.yml`

Good luck!
