from Bio.Align.Applications import MuscleCommandline

muscle_exe = r"C:\Users\CRACKID\Desktop\Util\muscle.exe"
cmd_line = MuscleCommandline(muscle_exe, input="HBA.all.fasta", out="HBA.aln", clw="")

print(cmd_line)

cmd_line()

