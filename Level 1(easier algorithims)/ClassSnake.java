public class ClassSnake{

  private int height = 50;
  private int width = 50;

  public ClassSnake(int height, int width){
      this.height = height;
      this.width = width;
  }

  public String getHeightVisualize(){
    int i;
    String output = "";
    for(i=0; i<height; i++){
      output += "x";
    }
    return output;
  }

  public int getWidth(){
    return width;
  }

}



