public class Referencia {
    private Aluno a1 , a2;
 
   
    /**
     * @param string
     */
    public Referencia (String string) {
     a1 = new Aluno ("Carlos" ,20);
     a2 = new Aluno (  "Ana" , 23 );
     System.out.println("O nome do aluno a1 é " + a1.recuperarNome());
     System.out.println("O nome do aluno a2 é " + a2.recuperarNome());
     a2 = a1;
     a2.definirNome( "Flávia");
     System.out.println("O nome do aluno a1 é " + a1.recuperarNome());
     manipulaAluno ( a1, "Márcia" );
     System.out.println("O nome do aluno a1 é " + a1.recuperarNome());
    }
    public void manipulaAluno ( Aluno aluno, String string ) {
     aluno.definirNome(string);
    }
}

