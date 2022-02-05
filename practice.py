from Bio.Align.Applications import MuscleCommandline

muscle_exe = r"C:\Users\CRACKID\Desktop\Util\muscle_v3.exe"
cmd_line = MuscleCommandline(muscle_exe, input="HBA.all.fasta", out="HBA.aln", clw=True)
print(cmd_line)

stdout, stderr = cmd_line()
