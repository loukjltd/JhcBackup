package com.jhc.abstractClass;

public abstract class DBOperator {
    public abstract void connection();
    public void open(){
        System.out.println("Open Database.");
    }
    public void use(){
        System.out.println("Using Database.");
    }
    public void close(){
        System.out.println("Close Database.");
    }

    public void process(){
        connection();
        open();
        use();
        close();
    }

    public static void main(String[] args) {
        new MySqlOperator().process();
        System.out.println();
        new OracleOperator().process();
        System.out.println();
        new MicrosoftAccessOperator().process();
    }
}


class MySqlOperator extends DBOperator {

    @Override
    public void connection() {
        System.out.println("Established connection with MySQL.");
    }
}

class OracleOperator extends DBOperator {
    @Override
    public void connection() {
        System.out.println("Established connection with Oracle.");
    }
}

class MicrosoftAccessOperator extends DBOperator {
    @Override
    public void connection() {
        System.out.println("Established connection with Microsoft Access.");
    }
}
